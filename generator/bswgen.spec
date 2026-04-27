# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for bswgen.exe
# Run from project root:
#   PYTHONPATH=core pyinstaller generator/bswgen.spec --distpath build/dist
#
# Mirrors V25.10 ORIENTAISBswGen.exe layout: each BSW module's
# .py + .jinja get added as data files; Common helpers are bundled
# as code (so PyInstaller PYZ holds them).
import os
import sys
from pathlib import Path

ROOT = Path(SPECPATH).resolve().parent  # project root
GEN = ROOT / 'generator'
CORE = ROOT / 'core'

block_cipher = None

# Add data files: every per-BSW-module dir under generator/modules/
data_files = []
modules_dir = GEN / 'modules'
for mod_dir in modules_dir.iterdir():
    if not mod_dir.is_dir() or mod_dir.name.startswith(('__','.','tests')):
        continue
    # Walk to add .py + .jinja preserving relative path
    for f in mod_dir.rglob('*'):
        if f.is_file() and f.suffix in ('.py', '.jinja') and '__pycache__' not in f.parts:
            rel_dir = f.parent.relative_to(modules_dir.parent)
            data_files.append((str(f), str(rel_dir)))

# Common templates
common_tmpl = CORE / 'Common' / 'templates'
for f in common_tmpl.glob('*.jinja'):
    data_files.append((str(f), 'Common/templates'))

a = Analysis(
    [str(GEN / '__main__.py')],
    pathex=[str(CORE), str(GEN)],
    binaries=[],
    datas=data_files,
    hiddenimports=[
        'Common',
        'Common.BswBase',
        'Common.Public',
        'Common.CodeGenerator',
        'Common.Context',
        'Common.J2Filters',
        'Common.arxmlparse',
        'Common.arxmlparse.loader',
        'Common.arxmlparse.constant.BswPathConstant',
        'Common.arxmlparse.cache.BswModuleCache',
        'Common.arxmlparse.artop',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='bswgen',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
