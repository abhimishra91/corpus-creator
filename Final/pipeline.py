import os
from docx2text import parse_docx2txt
from pdf2text import parse_pdf2txt


# Function to split the files and send them to different parsers
def pipeline(path):
    text_complete = str()
    text_out_pdf = str()
    text_out_doc = str()
    if path == "": path = os.getcwd() + "\\" #if no pdfDir passed in
    for file in os.listdir(path): # iterate through file in specified path
        file_extension = file.split(".")[-1]
        filename = path + file
        if file_extension == "pdf":
            text_out_pdf = parse_pdf2txt(filename) #get string of text content of pdf
        else:
            text_out_doc = parse_docx2txt(filename)
        text_complete = text_complete + text_out_pdf + text_out_doc
    return text_complete