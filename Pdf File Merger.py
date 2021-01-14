'''Requirements:
                pip install PyPDF2'''
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# Ask user the path to the directory where the PDFs are
PDF_Directory = input('Enter the directory of the PDFs to be merged:\n')

# Set the script's working directory to the location of the PDFs
os.chdir(PDF_Directory)

# Get a list of all PDF's fullPaths
pdf_to_merge = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_to_merge.append(filename)
        print(f'adding {filename} to list')
    else:
        print(f'\n{filename} is not a PDF file.\n')

print('\n')
pdfWriter = PdfFileWriter()

for filename in pdf_to_merge:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfFileObj.close
    print(f'{filename} read successfully')

print('\n\nPlease wait. This might take a few seconds...\n')
pdfOutput = open(PDF_Directory + '.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
input('''A new combined PDF file has been created beside the folder.
Press Enter to exit''')
