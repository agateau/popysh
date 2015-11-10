import subprocess


class Output(object):
    def __init__(self, proc, outf, errf):
        self._proc = proc
        self._outf = outf
        self._errf = errf
        self.returncode = proc.returncode

    def lines(self):
        return self._outf.decode().splitlines()

    def __repr__(self):
        return self._outf.decode()

    def bytes(self):
        return self._outf


class Wrap(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def __call__(self, *args, **kwargs):
        """
        kwargs:
        - merge_stderr: set to True to mix stderr in stdout
        - input: inptu to pipe in stdin (can be str or bytes)
        """
        cmd_args = [self.cmd]

        input_data = kwargs.get('input')
        if input_data:
            stdin = subprocess.PIPE
            if isinstance(input_data, str):
                input_data = input_data.encode()
        else:
            stdin = None
        stdout = subprocess.PIPE
        if kwargs.get('merge_stderr') == True:
            stderr = subprocess.STDOUT
        else:
            stderr = subprocess.PIPE

        for arg in args:
            if type(arg) in (list, tuple):
                cmd_args.extend(arg)
            else:
                cmd_args.append(str(arg))

        proc = subprocess.Popen(cmd_args, stdin=stdin, stdout=stdout,
                                stderr=stderr)
        outf, errf = proc.communicate(input=input_data)
        return Output(proc, outf, errf)
