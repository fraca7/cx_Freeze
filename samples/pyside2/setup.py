"""
A simple setup script to create an executable using PySide2. This also
demonstrates how to use excludes to get minimal package size.

test_pyside2.py is a very simple type of PySide2 application.

Run the build process by running the command 'python setup.py build'

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the application.
"""

import sys

from cx_Freeze import Executable, setup

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    "build_exe": {
        # exclude packages that are not really needed
        "excludes": [
            "tkinter",
            "unittest",
            "email",
            "http",
            "xml",
            "pydoc",
        ]
    }
}

executables = [Executable("test_pyside2.py", base=base)]

setup(
    name="simple_PySide2",
    version="0.4",
    description="Sample cx_Freeze PySide2 script",
    options=options,
    executables=executables,
)
