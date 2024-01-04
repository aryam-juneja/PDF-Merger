# import required libraries
from PyPDF2 import PdfWriter
import click
import os
from modules import *

@click.group()
def commands():
    pass

# merge files
@click.command()
@click.argument('files', required=False, nargs=-1, type=click.Path())
@click.option('--cat', nargs=1, type=click.Path())
def merge(files, cat):
    merger = PdfWriter()

    #for file names provided as arguments
    if files is not None:
        for file in files:
            append_to_list(os.path.join(os.getcwd(), add_ext(file)))

    # throw exception
    if len(get_list()) == 0 or len(get_list()) == 1:
        print("No. of Files to merge:", len(get_list()), '\n')
        print("Cannot perform merge operation. Please add files to merge.")
        return
    
    # merging algo
    for pdf in get_list():
        merger.append(pdf)
    
    if cat is None:
        cat = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    else: 
        cat = click.prompt('Enter the name of the merged file', type=click.Path(), default=cat)
    merger.write(add_ext(cat))
    merger.close()
    store_history(cat)
    clear_list()

# add files
@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def add(files):
    for file in files:
        if(search_selection(add_ext(file))):
            append_to_list(os.path.join(os.getcwd(), add_ext(file)))
        else:
            click.echo((click.style("File not found: ", fg='red')) + (click.style(file, fg='yellow')))
        
@click.command()
def list_sel():
    click.echo(click.style("List of the selected files:\n"))
    for file in get_list(): 
        print(file)

# list files in the open directory
@click.command()
def list_dir():
    click.echo(click.style("List of the PDF files in the open directory:\n"))
    i = 1
    for x in os.listdir():      # forms a list for all the files present in the directory
        if x.endswith(".pdf"):  # picks out the list members with '.pdf extention'
            append_to_list(x)
            print(i,'. ',x)
            i += 1

# to change the order of the files
@click.command()
@click.argument('order')
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
    # pdfList.clear()
    click.echo(click.style("Selcetion cleared successfully!"))

@click.command()
@click.argument('idx')
def remove(idx):
    idx.split(" ")
    for i in idx:
        remove_selection(i-1)

commands.add_command(merge)
commands.add_command(add)
commands.add_command(list_sel)
commands.add_command(list_dir)
commands.add_command(reorder)
commands.add_command(clear)
commands.add_command(remove)

if __name__ == "__main__":
    commands()