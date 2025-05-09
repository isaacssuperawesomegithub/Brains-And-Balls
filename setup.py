"""
Creates executable. 

Use `python setup.py build` to create exe.
"""


import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Brains and Balls",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["art"]}},
    executables = executables

    )