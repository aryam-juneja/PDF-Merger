import datetime
import json
import os

pdfList = open('pdfList.txt', 'r+').read().splitlines()

# get list of list file
def get_list(filename='pdfList.txt'):
    return open(filename, 'r+').read().splitlines()

# add file to list file
def appdent_to_list(file):
    with open('pdfList.txt', 'a+') as f:
        f.write(file + '\n')
        f.close()

# history dump
def store_history(name, filename='history.json'):
    with open(filename, 'r+') as file:

        file_data = json.load(file)
        file_data['history'].append({
            'name-merged': name,
            'files-merged': get_list(),
            'date': datetime.datetime.now()
        })
        file.seek(0)
        json.dump(file_data, file, indent=4)

# check if the file exists and is a pdf
def search_selection(file):
    if file in os.listdir and file.endswith(".pdf"):
        return True
    return False

#get filename only from the path
def get_filename(file):
    return file.split('/')[-1]

#add extension if no extension is present
def add_ext(file):
    if file.endswith(".pdf"):
        return file
    return file + '.pdf'