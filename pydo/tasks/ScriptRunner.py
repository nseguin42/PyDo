import asyncio
import subprocess

from pydo.config.Colors import Colors
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
            return asyncio.run(self.run_bash_script(script))
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

    async def run_bash_script_noninteractively(self, script: Script):
        # TODO
        return await self.run_bash_script_interactively(script)

    async def run_bash_script(self, script: Script):
        self.info("$ " + script.script)
        if script.interactive:
            return await self.run_bash_script_interactively(script)
        else:
            return await self.run_bash_script_noninteractively(script)

    async def log_stdout(self, stream, log_list=None):
        # Read lines from the stream and print them
        while True:
            line = await stream.readline()
            if not line:
                break
            line = line.decode().rstrip()
            self.info(line, Colors.OKCYAN)
            if log_list:
                log_list.append(line)
            log_list.append(line)

    async def log_stderr(self, stream, log_list=None):
        # Read lines from the stream and print them
        while True:
            line = await stream.readline()
            if not line:
                break
            line = line.decode().rstrip()
            self.warn(line)
            if log_list:
                log_list.append(line)
