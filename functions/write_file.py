import os

def write_file(working_directory, file_path, content):
        
    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        return 2
    if os.path.isdir(target_dir) == True:
        print(f'Error: Cannot write to "{file_path}" as it is a directory')
        return 2

    while (1):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            print("File doesn't exist. Creating file...")
            f.write(content)
            print(f'Successfully wrote to "{os.path.dirname(file_path)}" ({len(content)} characters written)')
            break
        except:
            return ("File exists")
        with open(os.path.dirname(file_path), "w") as f:
            f.write(content)
            print(f'Successfully wrote to "{os.path.dirname(file_path)}" ({len(content)} characters written)')
            return