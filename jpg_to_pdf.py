from PIL import Image
import sys


def convert_to_pdf(path):
    image = Image.open(path)
    pdf = image.convert('RGB')
    pdf.save("converted.pdf")


if __name__ == '__main__':
    args = sys.argv
    convert_to_pdf(args[1])
