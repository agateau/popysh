import os
import shutil

from popysh.systemcommands import SystemCommands


cd = os.chdir
cp = shutil.copyfile


def create(name, content=''):
    with open(name, 'w') as f:
        f.write(content)


touch = create


def mkdir(dirname, parents=False, mode=0o777):
    if parents:
        os.makedirs(dirname, mode=mode, exist_ok=True)
    else:
        os.mkdir(dirname, mode=mode)


syscmd = SystemCommands()
