def test_ls():
    from popysh.systemcommands import ls
    ls()

def test_pipe():
    from popysh.systemcommands import md5sum
    out = str(md5sum(input='bla'))
    assert out == '128ecf542a35ac5270a87dc740918404  -\n'
