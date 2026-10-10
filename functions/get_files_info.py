import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        is_target_dir_valid = os.path.commonpath([absolute_path, target_dir]) == absolute_path
        if not is_target_dir_valid:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        

    except Exception as e:
        return f"Error: {e}"


    try:
        contents_of_dir = os.listdir(target_dir)
        if directory == ".":
            directory_data = f"Result for current directory:"
        else:
            directory_data = f"Result for '{directory}' directory:"
        for file in contents_of_dir:
            file_path = os.path.normpath(os.path.join(target_dir, file))
            file_name = file
            file_size = os.path.getsize(file_path)
            is_file_a_dir = os.path.isdir(file_path)
            file_data = f"- {file_name}: file_size={file_size} bytes, is_dir={is_file_a_dir}"
            directory_data = "\n".join([directory_data, file_data])

        return directory_data

    except Exception as e:
        return f"Error: {e}"


    