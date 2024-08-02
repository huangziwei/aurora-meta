# app.spec
# PyInstaller spec file for OS Detector App

# Import the necessary module from PyInstaller
from PyInstaller.utils.hooks import copy_metadata
import os
import platform

# Collect all dependencies
a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pkgutil'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # This sets windowed mode
)

if platform.system() == "Darwin":
    app = BUNDLE(
        exe,
        name='app.app',
        icon=None,  # You can specify an icon file here
        bundle_identifier=None,
        info_plist={
            'CFBundleName': 'OSDetectorApp',
            'CFBundleDisplayName': 'OSDetectorApp',
            'CFBundleVersion': '0.1.0',
            'CFBundleShortVersionString': '0.1.0',
            'LSUIElement': '1',  # Hide dock icon if necessary
        },
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='app',
    )
else:
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='app',
    )
