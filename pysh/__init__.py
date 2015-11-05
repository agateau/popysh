import subprocess


class _Wrap(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def __call__(self, *args, **kwargs):
        cmd_args = [self.cmd]
        cmd_args.extend(args)
        for key, value in kwargs.items():
            option_name = key.replace('_', '--')

            if value == False:
                option_name = 'no-' + option_name

            if len(key) == 1:
                option_name = '-' + option_name
            else:
                option_name = '--' + option_name

            cmd_args.append(option_name)
            if type(value) is not bool:
                cmd_args.append(str(value))
        return subprocess.check_output(cmd_args).decode()


def wrap(cmd):
    return _Wrap(cmd)
