"""bswval CLI — `python -m validator -m <Module> -i <project>`.

Mirrors V25.10 ORIENTAISBswVal.exe CLI: load workspace ARXML into
`Common.arxmlparse.artop.def_elements`, then for each requested module,
look up `Bsw.<Module>.<Module>Register.getModuleArxmlValidator()` and
run all its `@RuleHandler`-decorated methods.
"""
from __future__ import annotations
import argparse
import importlib
import os
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
# Add validator/ to sys.path so `from Bsw.MemIf import ...` resolves.
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog='bswval',
        description='AUTOSAR ECUC validator (replaces V25.10 ORIENTAISBswVal.exe)',
    )
    p.add_argument('-i', '--input', required=True, metavar='PROJECT',
                   help='input project directory (workspace)')
    p.add_argument('-m', '--module', action='append', metavar='MODULE',
                   help='BSW module(s) to validate; may repeat. Default: all loaded.')
    p.add_argument('-o', '--output', default='output',
                   help='output directory for JSON validation report (default: output/)')
    p.add_argument('--target', default=None, help='target MCU/platform (optional)')
    p.add_argument('-v', '--verbose', action='store_true')
    args = p.parse_args(argv)

    print('**** Validator started ****')
    print('[INFO] Run python -m validator')
    print(f'[INFO] Parameters : {sys.argv}')

    t0 = time.time()

    # 1. Load ARXML project
    from Common.arxmlparse.loader import load_project
    project_path = Path(args.input).resolve()
    if not project_path.exists():
        print(f'[ERROR] input project not found: {project_path}')
        return 2
    print(f'[INFO] Loading ARXML project: {project_path}')
    modules = load_project(project_path)
    print(f'[INFO] Loaded {len(modules)} ECUC module(s); parse time: {time.time()-t0:.3f}(s)')

    # 2. Determine which modules to validate
    requested = args.module or [m.shortName for m in modules]
    print(f'[INFO] Modules to validate: {requested}')

    # 3. For each module, run its validator
    from Common.ArxmlValidator import dict_message
    all_results = []
    for mod_name in requested:
        try:
            register_mod = importlib.import_module(f'Bsw.{mod_name}.{mod_name}Register')
        except ImportError as e:
            print(f'[WARN] no validator registered for {mod_name}: {e}')
            continue
        if not hasattr(register_mod, 'getModuleArxmlValidator'):
            print(f'[WARN] {mod_name}Register missing getModuleArxmlValidator()')
            continue
        v = register_mod.getModuleArxmlValidator()
        print(f'[INFO] [{mod_name}]: Start running rules')
        v.runRules(changeTargetDefPath='')
        results = v.get_results()
        all_results.extend([(mod_name, *r) for r in results])
        print(f'[INFO] [{mod_name}]: All rules executed; {len(results)} finding(s)')

    # 4. Summary
    print()
    print('=' * 70)
    if not all_results:
        print(f'**** Total Count: critical: 0 error: 0 warning: 0  (PASS) ****')
    else:
        levels = {1: 'INFO', 2: 'WARNING', 4: 'ERROR', 8: 'CRITICAL'}
        counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0}
        for mod, rule_id, _ in all_results:
            rec = dict_message.get(rule_id, {})
            lvl = levels.get(rec.get('level', 4), 'ERROR')
            counts[lvl] += 1
        print(f'**** Total Count: critical: {counts["CRITICAL"]} '
              f'error: {counts["ERROR"]} '
              f'warning: {counts["WARNING"]} '
              f'info: {counts["INFO"]} ****')

    print(f'[INFO] Total time: {time.time()-t0:.3f}(s)')
    print('**** Validator finished ****')
    # Exit non-zero if any ERROR or CRITICAL — useful for CI.
    fail = sum(1 for _, rule_id, _ in all_results
               if dict_message.get(rule_id, {}).get('level', 4) >= 4)
    return 1 if fail else 0


if __name__ == '__main__':
    sys.exit(main())
