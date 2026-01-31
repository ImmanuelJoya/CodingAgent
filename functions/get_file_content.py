import os 
from config import MAX_CHARS
def get_file_content(working_dircetory, file_path):
    abs_working_dir = os.path.abspath(working_dircetory)
    abs_file_path = os.path.abspath(os.path.join(working_dircetory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is outside the working directory."
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a valid file."
    
    file_content_string = ""
    with open(abs_file_path, 'r') as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += (f'[...File "{file_path}" truncated after {MAX_CHARS} characters...]')
    return file_content_string