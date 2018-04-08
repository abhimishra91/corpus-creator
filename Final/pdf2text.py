from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

# Function to change the pdf file to text file
def parse_pdf2txt(filename, pages=None):
    if not pages:
        page_number = set()
    else:
        page_number = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(filename, 'rb')
    for page in PDFPage.get_pages(infile, page_number):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    #output.close
    return text