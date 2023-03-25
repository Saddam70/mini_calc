from cx_Freeze import setup, Executable

setup(name="Calculator",
        version = "0.1",
        executable = [Executable("Calculator.py")]
    )
# setup(name="calculator",
#         version="0.1",
#         description = "calculate",
#         executable = [Executable("Calculator.py")]
#     )on 