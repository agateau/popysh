from nose.tools import eq_


def test_ls():
    from popysh.syscmd import ls
    ls()

def test_stdin_stdout():
    from popysh.syscmd import md5sum
    out = str(md5sum(input='bla'))
    eq_(out, '128ecf542a35ac5270a87dc740918404  -\n')

def test_as_lines():
    from popysh.syscmd import cat
    lines = cat(input='bla\nbli').as_lines()
    eq_(lines, ['bla', 'bli'])

def test_returncode():
    from popysh.syscmd import ls
    proc = ls('/does-not-exist')
    returncode = proc.run()
    assert returncode != 0

def test_pipe():
    from popysh.syscmd import cat, grep, tr
    out = cat(input='bla\nbli\nblo') \
        .pipe(grep('bl[ai]')) \
        .pipe(tr('b', 'c')) \
        .as_bytes()

    eq_(out, 'cla\ncli\n')
