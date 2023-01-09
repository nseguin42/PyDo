import asyncio
import subprocess

from pydo.config.ScriptRunnerConfig import ScriptRunnerConfig
from pydo.models.Script import Script
from pydo.tasks.Task import Task


class ScriptRunner(Task):
    config: ScriptRunnerConfig
    script: Script

    def __init__(self, config: ScriptRunnerConfig):
        super().__init__(config)
        self.script = config.script

    def run(self):
        self.run_script(self.script)

    def run_script(self, script: Script):
        if script.lang == "bash" or script.lang == "sh":
            return self.run_bash_script(script)
        else:
            raise ValueError(f"Unsupported script language: {script.lang}")

    async def run_bash_script_interactively(self, script: Script):
        process = await asyncio.create_subprocess_shell(
            script.script,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout_list = []
        stderr_list = []

        await asyncio.gather(
            self.log_stdout(process.stdout, stdout_list),
            self.log_stderr(process.stderr, stderr_list),
        )

        await process.wait()

        return "".join(stdout_list)

    def run_bash_script_noninteractively(self, script: Script):
        process = subprocess.run(
            script.script,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        if process.stdout:
            self.info(process.stdout)
        if process.stderr:
            self.warn(process.stderr)

        return process.stdout

    def run_bash_script(self, script: Script):
        self.info("$ " + script.script)
        if script.interactive:
            return asyncio.run(self.run_bash_script_interactively(script))
        else:
            return self.run_bash_script_noninteractively(script)

    async def log_stdout(self, stream, log_list):
        # Read lines from the stream and print them
        while True:
            line = await stream.readline()
            if not line:
                break
            line = line.decode().rstrip()
            self.info(line)
            log_list.append(line)

    async def log_stderr(self, stream, log_list):
        # Read lines from the stream and print them
        while True:
            line = await stream.readline()
            if not line:
                break
            line = line.decode().rstrip()
            self.info(line)
            log_list.append(line)
