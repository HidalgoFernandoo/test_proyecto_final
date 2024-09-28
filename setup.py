from cx_Freeze import setup, Executable

setup(
    name="test",
    version="0.1",
    executables=[Executable("programa.py", base="Win32GUI")]
)
