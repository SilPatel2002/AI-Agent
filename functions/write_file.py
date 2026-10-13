import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_abs_path, file_path))
        is_target_file_path_valid = os.path.commonpath([working_abs_path, target_file_path]) == working_abs_path
        if not is_target_file_path_valid:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        
        parent_directory = os.path.dirname(target_file_path)

        os.makedirs(parent_directory, exist_ok=True)

        with open(target_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'