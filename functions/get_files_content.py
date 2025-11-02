import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    paths = {
        "working_directory": os.path.abspath(working_directory),
        "file_path": os.path.abspath(os.path.join(working_directory, file_path))
    }

    if not paths.get("file_path").startswith(paths.get("working_directory")):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(paths.get("file_path")):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        file_size = os.path.getsize(paths.get("file_path"))
        with open(paths.get("file_path"), "r") as file:
            if file_size > MAX_CHARS:
                content = file.read(MAX_CHARS)
                content += f'[...File "{file_path}" truncated at 10000 characters]'
                return content
            else:
                return file.read()
    except Exception as e:
        return f"Error: Failed to read file ({e}): ${file_path}"
