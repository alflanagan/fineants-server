import argparse
from typing import Iterable

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTContainer, LTTextLine, LTPage


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


def get_text(pdf_file: open) -> Iterable[str]:
    """
    Reads the open PDF file and returns an Iterable of the strings found.

    Does not close `pdf_file`!
    """
    lines = []
    pages = extract_pages(pdf_file)
    for page_layout in pages:  # type: LTPage
        for element in page_layout:  # type: LTContainer
            if isinstance(element, LTTextBoxHorizontal):
                for line in element:  # type: LTTextLine
                    lines.append(line.get_text())
    return lines
