import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    paths = {
        "working_directory": os.path.abspath(working_directory),
        "file_path": os.path.abspath(os.path.join(working_directory, file_path))
    }

    if not paths.get("file_path").startswith(paths.get("working_directory")):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(paths.get("file_path")):
        return f'Error: File "{file_path}" not found.'
    if not paths.get("file_path").endswith(".py"):
        return f'Error: File "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python", paths["file_path"]] + args,
            cwd=paths["working_directory"],
            capture_output=True,
            text=True,
            timeout=30
        )
        output_parts = []
        if result.stdout:
            output_parts.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output_parts.append(f"STDERR: {result.stderr}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        if not output_parts:
            return "No output produced."
        return "\n".join(output_parts)
    except subprocess.TimeoutExpired:
        return "Error: Process timed out after 30 seconds."
    except Exception as e:
        return f"Error: {str(e)}"