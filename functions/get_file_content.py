import os
from config import MAX_CHARACTERS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_abs_path, file_path))
        is_target_file_path_valid = os.path.commonpath([working_abs_path, target_file_path]) == working_abs_path
        if not is_target_file_path_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

    except Exception as e:
        return f'Error: {e}'


    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARACTERS)

        # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'

            return file_content_string

    except Exception as e:
        return f'Error: {e}'



schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the content written inside of a specific file within the working directory. Content is returned up to 10000 characters. Content is specified to be truncated if the file contains more than 10000 characters",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read content from, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}

    