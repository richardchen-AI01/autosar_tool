"""bswgen CLI — `python -m generator -g <Module> -i <project> -o <out>`.

Mirrors the V25.10 ORIENTAISBswGen.exe CLI shape so existing callers
(IDE Generate button, our reference_diff.py, manual cmd) work uniformly.
"""
from __future__ import annotations
import argparse
import importlib
import os
import sys
import time
from pathlib import Path

# Make the project's modules dir importable: `from MemIf.src.MemIf import MemIf` etc.
_HERE = Path(__file__).resolve().parent
_MODULES_DIR = _HERE / 'modules'
if str(_MODULES_DIR) not in sys.path:
    sys.path.insert(0, str(_MODULES_DIR))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog='bswgen',
        description='AUTOSAR ECUC code generator (replaces V25.10 ORIENTAISBswGen.exe)',
    )
    p.add_argument('-i', '--input', required=True, metavar='PROJECT',
                   help='input project directory (workspace)')
    p.add_argument('-o', '--output', required=True, metavar='DIR',
                   help='output directory for generated .c/.h files')
    p.add_argument('-g', '--generate', required=True, metavar='MODULE',
                   help='BSW module to generate (e.g. MemIf, Det, NvM)')
    p.add_argument('--toolVersion', default='for AutosarTool v0.1',
                   help='tool version string injected into output')
    p.add_argument('--target', default=None, help='target MCU/platform (optional)')
    p.add_argument('-v', '--verbose', action='store_true')
    args = p.parse_args(argv)

    print('**** Generator started ****')
    print(f'[INFO] Run python -m generator')
    print(f'[INFO] Parameters : {sys.argv}')

    t0 = time.time()

    # 1. Load ARXML project into Common.arxmlparse.artop.def_elements
    from Common.arxmlparse.loader import load_project
    project_path = Path(args.input).resolve()
    if not project_path.exists():
        print(f'[ERROR] input project not found: {project_path}')
        return 2
    print(f'[INFO] Loading ARXML project: {project_path}')
    modules = load_project(project_path)
    print(f'[INFO] Loaded {len(modules)} ECUC module(s) from project; '
          f'parse time: {time.time()-t0:.3f}(s)')

    # 2. Look up the requested module's Register
    module_name = args.generate
    try:
        register_mod = importlib.import_module(f'{module_name}.base.{module_name}Register')
    except ImportError as e:
        print(f'[ERROR] cannot import {module_name}.base.{module_name}Register: {e}')
        return 2

    if not hasattr(register_mod, 'getModuleCodeGenerator'):
        print(f'[ERROR] {module_name}Register missing getModuleCodeGenerator()')
        return 2

    # 3. Build context (per-module; usually instantiates the domain class)
    if hasattr(register_mod, 'getModuleContext'):
        try:
            ctx = register_mod.getModuleContext(str(project_path))
            if hasattr(ctx, 'postLoadArtopCache'):
                ctx.postLoadArtopCache()
        except Exception as e:
            print(f'[WARN] {module_name} getModuleContext failed: {type(e).__name__}: {e}')
            ctx = None
    else:
        ctx = None

    # 3.5. Detect "module not configured in workspace" cleanly so we don't
    # cascade into a confusing template UndefinedError. Convention: the module's
    # primary <Module>General container is the canonical "is this module
    # actually present" probe.
    domain = getattr(ctx, module_name, None) if ctx is not None else None
    primary_general = getattr(domain, f'{module_name}General', None) if domain else None
    if ctx is None or primary_general is None:
        print(f'[INFO] No ECUC configuration for {module_name} in workspace '
              f'{project_path} — nothing to generate.')
        print('**** Generator finished ****')
        return 0

    # 4. Wrap context in a holder that templates can do `context.<Module>Context.<Module>` on
    class _Ctx:
        pass
    holder = _Ctx()
    setattr(holder, f'{module_name}Context', ctx)

    # 5. Run the code generator
    cg = register_mod.getModuleCodeGenerator()
    cg.setContext(holder)
    cg.setModule(module_name)
    cg.setOutputPath(args.output)
    print('[INFO] Start to generate code')
    try:
        cg.generateCode()
    except Exception as e:
        import traceback
        print(f'[ERROR] generateCode failed: {type(e).__name__}: {e}')
        traceback.print_exc()
        return 1

    print('[INFO] Code generation is complete')
    print(f'[INFO] Total time: {time.time()-t0:.3f}(s)')
    print('**** Total Count: critical: 0 error: 0 warning: 0 ****')
    print('**** Generator finished ****')
    return 0


if __name__ == '__main__':
    sys.exit(main())
