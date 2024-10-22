import os
from os import path, walk
import classes.detect_system as ds

#prog_lib_path = ds.project_path
lib_path = '/home/chris/PycharmProjects/TTA/classes'
prog_lib =[]
prog_paths = []
class ProgramLibrary:
    sys_info = ds.DetectSystem()
    def __init__(self) -> None:
        self.lib_path = lib_path
        self.prog_lib = prog_lib
        self.prog_paths = prog_paths

        for dirpath, dirnames, filenames in walk(str(lib_path)):

            for filename in filenames:
                if filename.endswith(".py"):
                    prog_lib.append(filename)
                    prog_paths.append(path.join(dirpath, filename))


ProgramLibrary()
print(prog_lib)
print(prog_paths)