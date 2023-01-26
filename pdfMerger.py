from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()


print()
print("List of the PDF files in the open directory:\n")

i = 1

pdfList = []
for x in os.listdir():
    if x.endswith(".pdf"):
        pdfList.append(x)
        print(i,'. ',x)
        i += 1

print()
print()
#print(pdfList)
fileNo = [int(x) for x in input("Enter the file no.s to merge:").split()]
print(fileNo)

# List of the files to merge
pdfMergeList = []

for x in range(len(fileNo)):
    pdfMergeList.append(pdfList[fileNo[x]-1])

i = 1
for x in range(len(pdfMergeList)):
    print(i,". ",pdfMergeList[x])
    i += 1

for pdf in pdfMergeList:
    merger.append(pdf)

merger.write("merged-PDF.pdf")
merger.close()