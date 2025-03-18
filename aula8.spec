# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Lista de arquivos de dados que devem ser incluídos
datas = [
    ('clique.mp3', '.'),
    ('calmaCALA.gif', '.'),
    ('clique.png', '.'),
    ('login.ico', '.')
]

a = Analysis(
    ['aula8.py'],  # Substitua pelo nome do seu script Python
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Calma Calabreso',  # Nome do executável
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Defina como False para não abrir um console
    icon='login.ico',  # Ícone do executável
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='aula8.py',  # Nome da pasta de saída
)