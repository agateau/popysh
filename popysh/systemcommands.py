import os
from popysh.wrap import Wrap

def _wrap_system_commands():
    dct = {}
    for dirs in os.environ['PATH'].split(os.pathsep):
        for name in os.listdir(dirs):
            cmd_name = name.replace('-', '_')
            dct[cmd_name] = Wrap(name)
    globals().update(dct)

_wrap_system_commands()
