# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for bswval.exe
# Run from project root:
#   PYTHONPATH=core pyinstaller validator/bswval.spec --distpath build/dist
import os
import sys
from pathlib import Path

ROOT = Path(SPECPATH).resolve().parent
VAL = ROOT / 'validator'
CORE = ROOT / 'core'

block_cipher = None

data_files = []
bsw_dir = VAL / 'Bsw'
for mod_dir in bsw_dir.iterdir():
    if not mod_dir.is_dir() or mod_dir.name.startswith(('__','.','tests')):
        continue
    for f in mod_dir.rglob('*'):
        if f.is_file() and f.suffix in ('.py', '.json') and '__pycache__' not in f.parts:
            rel_dir = f.parent.relative_to(bsw_dir.parent)
            data_files.append((str(f), str(rel_dir)))

a = Analysis(
    [str(VAL / '__main__.py')],
    pathex=[str(CORE), str(VAL)],
    binaries=[],
    datas=data_files,
    hiddenimports=[
        'Common',
        'Common.BswBase',
        'Common.Public',
        'Common.ArxmlValidator',
        'Common.base.BaseClass',
        'Common.base.BaseDecorator',
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
    name='bswval',
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
