import os


def write_file(working_directory, file_path, content):
    paths = {
        "working_directory": os.path.abspath(working_directory),
        "file_path": os.path.abspath(os.path.join(working_directory, file_path))
    }

    if not paths.get("file_path").startswith(paths.get("working_directory")):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        with open(paths.get("file_path"), "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as exception:
        return f"Error: Failed to write file ({file_path}): ${exception}"