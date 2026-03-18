# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        ('libs/libiconv.dll','.'),
        ('libs/libzbar-64.dll','.'),
    ],
    datas=[('assets', 'assets'),
           ('codigo_barras', 'codigo_barras'),
           ('data', 'data'),
           ('database', 'database'),
           ('interface', 'interface'),
           ('models', 'models'),
           ('repositories', 'repositories'),
           ('services', 'services')
    ],
    hiddenimports=['repositories', 'services', 'interface', 'database', 'data', 'codigo_barras', 'models'],
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
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
