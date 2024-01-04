import datetime
import json
import os

# pdfList = open('pdfList.txt', 'r+').read().splitlines()

# get list of list file
def get_list(filename='pdfList.txt'):
    return open(filename, 'r+').read().splitlines()

# add file to list file
def append_to_list(file):
    with open('pdfList.txt', 'a+') as f:
        f.write(file + '\n')
        f.close()

# history dumps
def store_history(name, filename='history.json'):
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'r+') as file:
                file_data = json.load(file)
        else:
            file_data = {'history': []}

        file_data['history'].append({
            'name-merged': name,
            'files-merged': get_filename(),
            'date and time': datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        })

        with open(filename, 'w') as file:
            json.dump(file_data, file, indent=4)

# check if the file exists and is a pdf
def search_selection(file):
    dir = os.listdir()
    if file in dir and file.endswith(".pdf"):
        return True
    return False

#get filename only from the path
def get_filename(file_list = get_list()):
    names = []
    
    for file in file_list:
        # file_list.replace(file, file.split('/')[-1])
        names.append(file.split('\\')[-1])
        
    return names

#add extension if no extension is present
def add_ext(file):
    if file.endswith(".pdf"):
        return file
    return file + '.pdf'

#clear the list
def clear_list(filename='pdfList.txt'):
    open(filename, 'w').close()

#remove file from the list
def remove_selection(idx, filename='pdfList.txt'):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line != get_list()[int(idx)-1]:
                f.write(line)
        f.truncate()