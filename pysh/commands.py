import os

from pysh import wrap

def cd(dirname):
    os.chdir(dirname)

_COMMANDS = 'cp', 'mv', 'rm', 'ln', 'find', 'ls', 'touch', 'git'
for cmd in _COMMANDS:
    globals()[cmd] = wrap(cmd)
