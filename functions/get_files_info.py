import os
def get_files_info(working_directory, directory= None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = ""
    if directory is None:
        # directory = working_directory
        abs_directory = os.path.abspath(working_directory)
    else:
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    
    if not abs_directory.startswith(abs_working_dir):
        return f"Error: Directory {directory} is outside the working directory {abs_working_dir}."
    
    final_response = ""
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(os.path.join(abs_directory, content))
        size = os.path.getsize(content_path) 
        final_response += f"Content: {content}, Is Directory: {is_dir}, Size: {size}\n"
    return final_response