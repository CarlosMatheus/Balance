from cx_Freeze import setup, Executable
import os.path
from os import listdir
from os.path import isfile, join, isdir

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

balance = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(balance, "balance.py")

__version__ = "1.1.0" # Todo: Put here the real version

# todo remember that to make this work, you have to change something on the file version on engine
class Files():
    all_files = []

    @classmethod
    def get_files(cls, dir):
        cls.all_files = []
        cls._get_files_r(dir)
        return cls.all_files

    #todo: chack if this fucntion is realy necessary:
    @classmethod
    def _get_files_r(cls, dir):
        onlyfiles = [os.path.join(dir, f) for f in listdir(dir) if isfile(join(dir, f))]
        onlydir = [os.path.join(dir, f) for f in listdir(dir) if isdir(join(dir, f))]
        cls.all_files += onlyfiles
        # for file in onlyfiles:
        #     lines = open(file).read().split("\n")
        #     for line in lines:
        #         commands = line.split(";")
        #         for command in commands:
        #             if "import" in command:
        #                 if command.startswith("from") or command.startswith("import"):
        #                     after_from = command.split("from")
        #                     parts = after_from.split("import")
        #                     if len(parts) == 1:
        #                         part = parts[0]
        #                         part
        #                     before_import = parts[]
        #                     words = line.split(" ")
        #                     if len(words) > 0:
        #                         if words[0] == "import":
        #                             words[0]
        #                         if words[0] == "from":
        for dir in onlydir:
            cls._get_files_r(dir)

dir = os.path.join(os.path.join(balance, "game"))

include_files = [dir] # you can just include all files you need passing the entire folder as da dependency
excludes = []
packages = ["pygame", "pygin", "asyncio"] # Here we just have to put libraries used on engine

setup(
    name = "balance",
    description='App Description',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable(file, base="Win32GUI")]
)
