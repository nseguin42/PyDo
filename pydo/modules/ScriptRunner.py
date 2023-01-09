import asyncio
import subprocess

from pydo.config.ScriptRunnerConfig import ScriptRunnerConfig
from modules.Module import Module
from pydo.models.Script import Script


class ScriptRunner(Module):
    config: ScriptRunnerConfig
    script: Script

    def __init__(self,
                 instance_name: str, config: ScriptRunnerConfig):
        super().__init__(instance_name, config)
        self.script = config.script

    def run(self):
        self.run_script(self.script)

    def run_script(self, script: Script):
        if script.lang == "sh" or script.lang == "bash":
            return self.run_bash_script(script)

        raise Exception(f"Unsupported script language: {script.lang}")

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
        self.info(script.script)
        if self.config.is_interactive:
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
