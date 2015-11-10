import subprocess


class Output(object):
    def __init__(self, output):
        self.output = output

    def lines(self):
        return self.output.splitlines()

    def __repr__(self):
        return self.output.decode()


class Wrap(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def __call__(self, *args, **kwargs):
        cmd_args = [self.cmd]
        for arg in args:
            if type(arg) in (list, tuple):
                cmd_args.extend(arg)
            else:
                cmd_args.append(str(arg))
        out = subprocess.check_output(cmd_args)
        return Output(out)
