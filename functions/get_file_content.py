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

