# Goals

Less magic:

- Wild-card only when you need them:

    from glob import glob
    from popysh.systemcommands import rm
    rm(glob('*.tmp'))

- No errors from files with spaces:

    from popysh.systemcommands import rm
    rm('file with space', 'another one')

Easy integration with Python:

    from popysh.systemcommands import find
    for idx, line in enumerate(find('-name', '*.py').lines()):
        print('{} {}'.format(idx, line.decode()))

# Tests

Run `nosetests` from root dir
