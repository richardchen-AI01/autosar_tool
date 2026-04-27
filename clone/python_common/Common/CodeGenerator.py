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

    def generateCode(self) -> None:
        """The main entry point. Render all Jinja templates listed in FilesList.jinja."""
        if self.module is None:
            raise RuntimeError("CodeGenerator.generateCode: module not set")
        t0 = time.time()

        # Locate this module's templates dir from MRO of caller
        templates_dir = self.__loadTemplateFolders()

        files_list_path = templates_dir / 'FilesList.jinja'
        if not files_list_path.exists():
            raise FileNotFoundError(f'FilesList.jinja not found at {files_list_path}')

        # Render FilesList.jinja with current context to know which files to emit
        from jinja2 import Environment, FileSystemLoader, StrictUndefined
        env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            undefined=StrictUndefined,
            keep_trailing_newline=True,
            trim_blocks=False,
            lstrip_blocks=False,
        )
        # Register custom filters from J2Filters
        try:
            from Common.J2Filters import register_filters
            register_filters(env)
        except ImportError:
            pass

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
            content = env.get_template(tpl_name).render(context=self.context)
            (out_dir / out_name).write_text(content, encoding='utf-8')
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
