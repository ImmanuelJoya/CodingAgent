# from functions.get_files_info import get_files_info 
# from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    working_dir = "calculator"
    # print(write_file(working_dir, "lorem.txt", "wait, this is a test!!"))
    print (write_file(working_dir, "pkg/morelorem.txt" , "hey wait, this is a test!"))
    # print (write_file(working_dir, "tmp/temp.txt", "this souldn't be allowed!"))

    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "/bin/cat"))
    
main()