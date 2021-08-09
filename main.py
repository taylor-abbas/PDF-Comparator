"""
Keep this python file in the same folder as the PDFs.
Run & just Input the names of the PDFs.

Author : Abbas Tailor
"""

import PyPDF2
import sys
import codecs
if sys.stdout.encoding != 'cp850':
    sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict') 

file = input("Input the name of the 1st file excluding .pdf => ")
file += '.pdf'
pdfFileObj = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdf1 = pdfReader.getPage(0)

file = input("Input the name of the 2nd file excluding .pdf => ")
file += '.pdf'
pdfFileObj = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdf2 = pdfReader.getPage(0)

p1 = pdf1.extractText().encode('UTF-8')
p2 = pdf2.extractText().encode('UTF-8')

if(p1 == p2):
    print("\nSame PDFs !!!\n")
else:
    print("\nChanges detected \n")
