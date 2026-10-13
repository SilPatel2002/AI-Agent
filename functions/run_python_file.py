import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_abs_path, file_path))
        is_target_file_path_valid = os.path.commonpath([working_abs_path, target_file_path]) == working_abs_path
        if not is_target_file_path_valid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file_path]
        if args is not None:
            command.extend(args)
        completed_process = subprocess.run(command, capture_output=True, cwd=working_abs_path, timeout=30, text=True)
        return_string = ""
        if completed_process.returncode != 0:
            return_string += f"Process exited with code {completed_process.returncode}\n"

        if completed_process.stdout is None:
            if completed_process.stderr is None:
                return_string += f"No output produced\n"

        if completed_process.stdout is not None:
            return_string += f"STDOUT: {completed_process.stdout}"

        if completed_process.stderr is not None:
            return_string += f"STDERR: {completed_process.stderr}"

        return return_string


    except Exception as e:
        return f"Error: executing Python file: {e}"