import os

from pysh import wrap

def cd(dirname):
    os.chdir(dirname)

def _wrap_from_path():
    for dirs in os.environ['PATH'].split(':'):
        for name in os.listdir(dirs):
            cmd_name = name.replace('-', '_')
            globals()[cmd_name] = wrap(name)

_wrap_from_path()
