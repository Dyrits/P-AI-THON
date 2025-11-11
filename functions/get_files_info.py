import os

def get_files_info(working_directory, directory="."):
    paths = {
        "working_directory": os.path.abspath(working_directory),
        "directory": os.path.abspath(os.path.join(working_directory, directory))
    }

    if not paths.get("directory").startswith(paths.get("working_directory")):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(paths.get("directory")):
        return f'Error: "{directory}" is not a directory'

    try:
        files_info = []

        for filename in os.listdir(paths.get("directory")):
            filepath = os.path.join(paths.get("directory"), filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )

        return "\n".join(files_info)
    except Exception as exception:
        return f"Error listing files: {exception}"
