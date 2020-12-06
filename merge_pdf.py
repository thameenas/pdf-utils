import sys

from PyPDF2 import PdfFileReader, PdfFileMerger


def merge(file_names):
    merged_pdf = PdfFileMerger()
    for file in file_names:
        pdf = open(file, "rb")
        merged_pdf.append(PdfFileReader(pdf))
    merged_pdf.write("merged.pdf")


if __name__ == '__main__':
    args = sys.argv
    merge(args[1:])
