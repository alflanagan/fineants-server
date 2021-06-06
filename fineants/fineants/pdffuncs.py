import argparse
from typing import Iterable

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal

# keeping this for now as example of lower-level parsing. better way is below it
# def get_text(fd: open) -> str:
#     output_string = StringIO()
#     parser = PDFParser(fd)
#     doc = PDFDocument(parser)
#     rsrcmgr = PDFResourceManager()
#     device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     for page in PDFPage.create_pages(doc):
#         interpreter.process_page(page)
#     return output_string.getvalue()


def get_text(fd: open) -> Iterable[str]:
    """
    Reads the open PDF file and returns an Iterable of the strings found.

    Does not close `fd`!
    """
    lines = []
    pages = extract_pages(opts.pdf_file)
    for page_layout in pages:
        for element in page_layout:
            if isinstance(element, LTTextBoxHorizontal):
                for line in element:
                    lines.append(line)
    return lines
