import cx_Freeze


executables = [cx_Freeze.Executable("_ignore/HelloPyGame.py")]

"""
"included_files" => must be anything inside assets
"""

cx_Freeze.setup(
    name="test",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": []
                           }
             },
    executables=executables
)
