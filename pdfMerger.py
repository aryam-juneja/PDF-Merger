# import required libraries
from PyPDF2 import PdfWriter
import datetime
import json
import click
import os

pdfList = []

# history dump
def store_history(name, filename='history.json'):
    with open(filename, 'r+') as file:

        file_data = json.load(file)
        file_data['history'].append({
            'name-merged': name,
            'files-merged': pdfList,
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

@click.group()
def commands():
    pass

# merge files
@click.command()
@click.argument('files', required=False, help='The name of the merged file')
@click.argument('cat',)
def merge(name, files, cat):
    merger = PdfWriter()
    if files is not None:
        files.split(" ")
        for file in files:
            pdfList.append(file + '.pdf')

    if len(pdfList) == 0 or 1:
        print("No. of Files to merge:", len(pdfList), '\n')
        print("Cannot perform merge operation. Please add files to merge.")
        return
    
    for pdf in pdfList:
        merger.append(pdf)
    
    # mergedName = input("Enter the name of the merged file:") + '.pdf'
    merger.write(name + '.pdf')
    merger.close()
    store_history(name)
    pdfList.clear()

# add files
@click.command()
@click.argument('file', prompt='Enter the name of the file/s to merge:', help='The name of the file/s to merge')
def add(file):
    file.split(" ")
    if(search_selection(file)):
        pdfList.append(os.path.join(os.getcwd(), add_ext(file)))
        
@click.command()
def list_sel():
    click.echo(click.style("List of the selected files:\n"))
    for file in pdfList: 
        print(file)

# list files in the open directory
@click.command()
def list_dir():
    click.echo(click.style("List of the PDF files in the open directory:\n"))
    i = 1
    for x in os.listdir():      # forms a list for all the files present in the directory
        if x.endswith(".pdf"):  # picks out the list members with '.pdf extention'
            pdfList.append(x)
            print(i,'. ',x)
            i += 1

@click.command()
@click.argument('order', prompt='Enter the order of the files to merge:', help='The order of the files to merge')
def reorder(order):
    order.split(" ")
    if len(order) != len(pdfList):
        print("The order of the files is not correct. Please check the order again.")
        return
    temp = []
    for i in order:
        temp.append(pdfList[int(i)-1])
    pdfList.clear()
    pdfList = temp.copy()

@click.command()
def clear():
    pdfList.clear()
    click.echo(click.style("Selcetion cleared successfully!"))

@click.command()
@click.argument('idx', prompt='Remove what laa?:', help='The name of the file to remove')
def remove(idx):
    idx.split(" ")
    for i in idx:
        pdfList.pop(int(i)-1)

if __name__ == "__main__":
    commands()