import sys

from PyPDF2 import PdfFileReader, PdfFileWriter


def remove(file_name, pages):
    pages_to_delete = [int(i) - 1 for i in pages.split(",")]
    pdf_file = PdfFileReader(file_name)
    output_pdf = PdfFileWriter()

    for i in range(pdf_file.getNumPages()):
        if i not in pages_to_delete:
            output_pdf.addPage(pdf_file.getPage(i))
    with open("removed.pdf", "wb") as f:
        output_pdf.write(f)


if __name__ == '__main__':
    args = sys.argv
    remove(args[1], args[2])
