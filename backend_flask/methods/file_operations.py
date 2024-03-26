import os
import shutil

def list_files(directory):
    return os.listdir(directory)

def move_file(source_directory, destination_directory, filename):
    source = os.path.join(source_directory, filename)
    destination = os.path.join(destination_directory, filename)
    if os.path.exists(source):
        shutil.move(source, destination)
        return {'status': 'success', 'message': f'{filename} moved successfully.'}
    else:
        return {'status': 'error', 'message': 'File does not exist.'}
