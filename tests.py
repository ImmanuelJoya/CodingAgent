from functions.get_files_info import get_files_info 

def main():
    working_dir = "calculator"
    root_contents = get_files_info(working_dir)
    print("Root Directory Contents:\n", root_contents)
    
    pkg_contents = get_files_info(working_dir, "pkg")
    print("pkg Directory Contents:\n", pkg_contents)
    
    pkg_contents = get_files_info(working_dir, "/bin")
    print("Attempt to access /bin Directory Contents:\n", pkg_contents)
    
    pkg_contents = get_files_info(working_dir, "../")
    print("Attempt to access ../ Directory Contents:\n", pkg_contents)
    
main()