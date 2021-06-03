from io import StringIO
import argparse

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def get_text(fd: open) -> str:
    output_string = StringIO()
    parser = PDFParser(fd)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
    return output_string.getvalue()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract text from a Wells Fargo statement PDF')
    parser.add_argument('pdf_file', type=lambda fname: open(fname, 'rb'), help='The PDF downloaded from Wells Fargo')

    opts = parser.parse_args()
    try:
        print(get_text(opts.pdf_file))
    finally:
        opts.pdf_file.close()
