import os

def write_file(working_directory: str, directory: str, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: File path {file_path} is outside the working directory {abs_working_dir}."
    if not os.path.isfile(abs_file_path):
        return f"Error: File {file_path} does not exist."