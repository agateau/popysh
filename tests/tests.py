def test_ls():
    from popysh.syscmd import ls
    ls()

def test_pipe():
    from popysh.syscmd import md5sum
    out = str(md5sum(input='bla'))
    assert out == '128ecf542a35ac5270a87dc740918404  -\n'
