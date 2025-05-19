# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/rocket_model/main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('src/rocket_model/gui/images/splash.png', 'gui/images'),
        ('src/rocket_model/gui/images/HornetLogo.png', 'rocket_model/gui/images'),
        ('src/rocket_model/config/atmospheric_properties.csv', 'rocket_model/config')
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
    name='RocketModel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
