# import required libraries
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
import os

# declared variable for PDFWriter, used to write in a PDF
merger = PdfWriter()


print()
print("List of the PDF files in the open directory:\n")

i = 1

pdfList = []


for x in os.listdir():      # forms a list for all the files present in the directory
    if x.endswith(".pdf"):  # picks out the list members with '.pdf extention'
        pdfList.append(x)
        print(i,'. ',x)
        i += 1

print()
print()

# list that takes integer input from user
fileNo = [int(x) for x in input("Enter the file no.s to merge:").split()]
print(fileNo)

# List of the files to merge
pdfMergeList = []

for x in fileNo:
    pdfMergeList.append(pdfList[x-1])

i = 1
for x in pdfMergeList:
    print(i,". ",x)
    i += 1

for pdf in pdfMergeList:
    merger.append(pdf)

pdfName = input("Enter the name of the merged file:") + '.pdf'

merger.write(pdfName)
merger.close()