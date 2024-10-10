# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\rocekt_model\\main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('src\\rocekt_model\\gui\\images\\HornetLogo.png', 'gui\\images'),
        ('src\\rocekt_model\\gui\\images\\splash.png', 'gui\\images')
        ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
