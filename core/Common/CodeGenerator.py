"""CodeGenerator — replaces V25.10 Common/CodeGenerator.pyd.

API surface (see autosar-cfg/_pyd_analysis/CodeGenerator.md):
  CodeGenerator class with __init__, __loadTemplateFolders,
  setContext, setModule, deleteOldFiles, generateCode

Behavior strings:
  '[%s]: All files are generated, time consumed: %s'
  '[%s]: Start to Generate file: %s'
  'The incremental generation directory is [%s]'

D1 STATUS: minimal walking-skeleton implementation that:
  1. accepts setContext / setModule from <Module>CodeGenerator subclass
  2. loads Jinja2 templates from <Module>/templates/
  3. reads FilesList.jinja to know which files to emit
  4. renders each template with the module's Context
  5. writes output files

This is enough for D3 walking-skeleton "MemIf 端到端走通" — output
correctness comes in M2.
"""
from __future__ import annotations
import os
import time
from pathlib import Path
from typing import Any, Optional


class CodeGenerator:
    """Base class for all <Module>CodeGenerator subclasses."""

    def __init__(self) -> None:
        self.context: Optional[Any] = None
        self.module: Optional[str] = None
        self._template_dirs: list[Path] = []
        self._output_path: Optional[Path] = None
        # Defaults match V25.10 reference output (see samples/.../config/MemIf_Cfg.h header)
        self._tool_version: str = 'for AutosarTool v0.1'
        self._mcu: str = 'S32K148'
        self._customer: str = 'iSoft'

    # ------------------------------------------------------------ public API

    def setContext(self, ctx: Any) -> None:
        """Subclass calls super().__init__() then framework sets context."""
        self.context = ctx

    def setModule(self, module_name: str) -> None:
        self.module = module_name

    def setOutputPath(self, path: str) -> None:
        self._output_path = Path(path)

    def deleteOldFiles(self) -> None:
        """Delete previously generated files for this module from output dir.
        D1 stub: no-op (M2 will read FilesList.jinja and delete only those)."""
        pass

    def generateCode(self, *args, **kwargs) -> None:
        """The main entry point. Render all Jinja templates listed in FilesList.jinja.

        Some module subclasses pass extras (e.g. Det's `incFileList`); we accept
        and currently ignore them — D2 walking-skeleton scope. M2 will use them
        for the IncGen / Externals.c handling.
        """
        if args:
            self._extra_args = args
        if kwargs:
            self._extra_kwargs = kwargs
        if self.module is None:
            raise RuntimeError("CodeGenerator.generateCode: module not set")
        t0 = time.time()

        # Locate this module's templates dir from MRO of caller
        templates_dir = self.__loadTemplateFolders()

        files_list_path = templates_dir / 'FilesList.jinja'
        if not files_list_path.exists():
            raise FileNotFoundError(f'FilesList.jinja not found at {files_list_path}')

        # Render FilesList.jinja with current context to know which files to emit.
        # Search path: module's own templates/ + Common's shared templates/.
        from jinja2 import Environment, FileSystemLoader, StrictUndefined
        common_templates = Path(__file__).resolve().parent / 'templates'
        search_dirs = [str(templates_dir)]
        if common_templates.is_dir():
            search_dirs.append(str(common_templates))
        env = Environment(
            loader=FileSystemLoader(search_dirs),
            undefined=StrictUndefined,
            keep_trailing_newline=True,
            trim_blocks=True,        # eat newline after {% ... %} blocks
            lstrip_blocks=True,      # strip leading whitespace before {% %}
        )
        # Register custom filters from J2Filters
        try:
            from Common.J2Filters import register_filters
            register_filters(env)
        except ImportError:
            pass
        # Inject Template_Base.jinja's expected globals (mirrors V25.10 defaults)
        import datetime as _dt
        env.globals.update({
            'ModuleFile':         '',                            # set per-file in render below
            'generateTime':       _dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'DefaultToolVersion': self._tool_version,
            'DefaultMcu':         self._mcu,
            'DefaultLicense':     '',
            'DefaultCustomer':    self._customer,
            # IncGen / user-code-block preservation: empty unless --inc-gen is wired
            'UserCodeDefinitions': {},
            # Cross-module memory-partition tag. Some module templates (e.g.
            # Det_Bswmd.arxml) interpolate it into MEMORY-SECTION short names
            # like VAR_CLEARED_{{EcucPartition}}_UNSPECIFIED. V25.10 leaves it
            # blank when no EcucPartition is wired — produces "VAR_CLEARED__"
            # which matches the bundled reference Det_Bswmd.arxml.
            'EcucPartition':       '',
        })

        files_list_text = env.get_template('FilesList.jinja').render(context=self.context).strip()

        out_dir = self._output_path or Path('output')
        out_dir.mkdir(parents=True, exist_ok=True)

        for line in files_list_text.splitlines():
            line = line.strip()
            if not line:
                continue
            # FilesList.jinja format: <output_filename>@#@<template_name>@#@<extra>
            parts = line.split('@#@')
            if len(parts) < 2:
                continue
            out_name, tpl_name = parts[0].strip(), parts[1].strip()
            if tpl_name.startswith('/'):
                tpl_name = tpl_name[1:]
            t_start = time.time()
            print(f'[INFO] [{self.module}]: Start to Generate file:\'{out_name}\'')
            env.globals['ModuleFile'] = out_name
            content = env.get_template(tpl_name).render(context=self.context)
            # Match V25.10 output line endings (CRLF on Windows-generated files).
            # newline='' on write keeps embedded line endings as-is.
            content = content.replace('\r\n', '\n').replace('\n', '\r\n')
            (out_dir / out_name).write_text(content, encoding='utf-8', newline='')
            print(f'[INFO] File:\'{out_name}\' is generated, time consumed: {time.time()-t_start:.3f}(s)')

        print(f'[INFO] [{self.module}]: All files are generated, time consumed: {time.time()-t0:.3f}(s)')

    # ------------------------------------------------------------ internals

    def __loadTemplateFolders(self) -> Path:
        """Walk caller's MRO to find <Module>/templates/ relative to subclass file."""
        import inspect
        for cls in type(self).__mro__:
            if cls is CodeGenerator or cls is object:
                continue
            try:
                cls_file = Path(inspect.getfile(cls))
            except (OSError, TypeError):
                continue
            # Subclass typically lives at <Module>/base/<Module>CodeGenerator.py
            tmpl = cls_file.parent.parent / 'templates'
            if tmpl.is_dir():
                return tmpl
        raise FileNotFoundError(f'templates/ dir not found via MRO of {type(self).__name__}')
