import subprocess


class Process(object):
    def __init__(self, args, input_data=None, merge_stderr=False):
        self._args = args
        self._input_data = input_data

        if merge_stderr:
            self._stderr = subprocess.STDOUT
        else:
            self._stderr = subprocess.PIPE

        if self._input_data:
            self._stdin = subprocess.PIPE
        else:
            self._stdin = None

        self._pipe_head = None

        self.returncode = -1

    def run(self, stdout=None):
        """
        Run the process, sends stdout to the process stdout by default or to
        the stdout argument if specified. `stdout` must be a file opened in
        write or append mode.

        Useful for long-time running commands.

        Returns the process return code.
        """
        self._create_proc(stdout=stdout)
        self._communicate()
        return self.returncode

    def as_bytes(self):
        """
        Run the process, returns its stdout as bytes
        """
        self._capture_output()
        return self.out

    def as_str(self):
        """
        Run the process, returns its stdout as a str
        """
        return self.as_bytes().decode()

    def as_lines(self):
        """
        Run the process, returns its stdout as a list of str
        """
        return self.as_str().splitlines()

    def __repr__(self):
        return self.as_str()

    def pipe(self, next_process):
        """
        Sends stdout of the current process into stdin of `next_process`.
        Returns a Process instance.

        `next_process` must *not* have any `input_data`, since its input is going
        to be the output of the current process.
        """
        assert next_process._input_data is None
        self._create_proc(stdout=subprocess.PIPE)
        if self._pipe_head is None:
            self._pipe_head = self

        next_process._stdin = self._proc.stdout
        next_process._pipe_head = self._pipe_head
        return next_process

    def _capture_output(self):
        self._create_proc(stdout=subprocess.PIPE)
        return self._communicate()

    def _create_proc(self, stdout=None):
        self._proc = subprocess.Popen(self._args, stdin=self._stdin, stdout=stdout, stderr=self._stderr)

    def _communicate(self):
        if self._pipe_head:
            self._pipe_head._write_stdin()
        self.out, self.err = self._proc.communicate(input=self._input_data)
        self.returncode = self._proc.returncode

    def _write_stdin(self):
        if self._input_data is not None:
            self._proc.stdin.write(self._input_data)
            self._proc.stdin.close()


class Wrap(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def __call__(self, *args, **kwargs):
        """
        kwargs:
        - merge_stderr: set to True to mix stderr in stdout
        - input: input to pipe in stdin (can be str or bytes)
        """
        cmd_args = [self.cmd]

        input_data = kwargs.get('input')
        if input_data:
            if isinstance(input_data, str):
                input_data = input_data.encode()
        merge_stderr = kwargs.get('merge_stderr', False)

        for arg in args:
            if type(arg) in (list, tuple):
                cmd_args.extend(arg)
            else:
                cmd_args.append(str(arg))

        return Process(cmd_args, input_data=input_data, merge_stderr=merge_stderr)
