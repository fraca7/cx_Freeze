"""A very simple setup script to create a single executable using Tkinter.

test_tkinter.py is a very simple type of Tkinter application.

Run the build process by running the command 'python setup.py build'

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the script without Python.
"""

import sys

from cx_Freeze import Executable, setup

base = "Win32GUI" if sys.platform == "win32" else None
executables = [Executable("test_tkinter.py", base=base)]

setup(
    name="test_tkinter",
    version="0.2",
    description="Sample cx_Freeze Tkinter script",
    executables=executables,
)
