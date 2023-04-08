import os

def list_files(current_path):
  if not os.path.isdir(current_path):
    print(current_path)
  else:  
    for file_name in os.listdir(current_path):
      file_name = os.path.join(current_path, name)

      list_files(file_name)
        
