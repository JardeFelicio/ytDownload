import sys
from xml.etree.ElementInclude import include
from cx_Freeze import setup, Executable

files=["git.ico","telaYtDownload.ui","git_white.ico"]



# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["PyQt5"],"include_files":["git.ico","telaYtDownload.ui","git_white.ico"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="YT Download",
    version="1.0",
    description="Realiza download de músicas e vídeos do YouTube",
    author="Jarde Felicio",
    options={"build_exe": build_exe_options},
    executables=[Executable("ytDownload.py", base=base,icon="git.ico"
)]
)