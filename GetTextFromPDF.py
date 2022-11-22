###########################################
#
# Script to Convert PDFs into Text information
# Code by Shiyu Hu
#
##########################################

# Import library
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfMerger

###################################
# Get the list of pdf files
##################################
PDF_list = []
pdf_name = "pdf1.pdf"
i = 0
while i < 19:
    i = i+1
    temp = list(pdf_name)
    temp[3] = str(i)
    string = "".join(temp)
    PDF_list += [string]
print("Here is the PDF list download:",PDF_list)


##################################################################
# Merge all PDFs into one PDF
##################################################################
merger = PdfMerger()
for pdf in PDF_list:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()


##################################################################
# Transfer PDF: result.pdf to image: out.JPG
##################################################################
# import module
# pip install PyMuPDF==1.18.9
import fitz
from typing import Tuple
import os

def convert_pdf2img(input_file: str, pages: Tuple = None):
    """Converts pdf to image and generates a file by page"""
    # Open the document
    pdfIn = fitz.open(input_file)
    output_files = []
    # Iterate throughout the pages
    for pg in range(pdfIn.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        # Select a page
        page = pdfIn[pg]
        rotate = int(0)
        # PDF Page is converted into a whole picture 1056*816 and then for each picture a screenshot is taken.
        # zoom = 1.33333333 -----> Image size = 1056*816
        # zoom = 2 ---> 2 * Default Resolution (text is clear, image text is hard to read)    = filesize small / Image size = 1584*1224
        # zoom = 4 ---> 4 * Default Resolution (text is clear, image text is barely readable) = filesize large
        # zoom = 8 ---> 8 * Default Resolution (text is clear, image text is readable) = filesize large
        zoom_x = 2
        zoom_y = 2
        # The zoom factor is equal to 2 in order to make text clear
        # Pre-rotate is to rotate if needed.
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        output_file = f"{os.path.splitext(os.path.basename(input_file))[0]}_page{pg+1}.png"
        pix.writePNG(output_file)
        output_files.append(output_file)
    pdfIn.close()
    summary = {
        "File": input_file, "Pages": str(pages), "Output File(s)": str(output_files)
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return output_files
if __name__ == "__main__":
    input_file = 'result.pdf'
    convert_pdf2img(input_file)




##########################################################
# Extract text from images
##########################################################
# intall tesseract (conda install -c conda-forge tesseract)
# To get the eng.traineddata file within the tessdata directory: wget https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata

# Import library
import pytesseract
import PIL.Image

# Assume a single uniform block of text (psm 6), set oem by default, based on what is available(oem 3)
myconfig = r"--psm 6--oem 3"
# Transfer image.png to text
# text = pytesseract.image_to_string(PIL.Image.open("result_page1.png"), config=myconfig)
# Get all of the text information in string
i = 0
temp = ""
while i < 19:
    i = i+1
    text = pytesseract.image_to_string(PIL.Image.open("result_page"+str(i)+".png"), config=myconfig)
    temp += text
# Convert strings to text.file
my_str = temp
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(my_str)
print("text has been save as result.txt")