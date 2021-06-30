from PyPDF2 import PdfFileWriter , PdfFileReader
from colorama import Fore
from time import sleep

def pdf_encrypt (file, password):
    # write in file
    parser = PdfFileWriter()
    # read the file
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    # set password
    parser.encrypt(password)
    with open(f"encrypt_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"[{Fore.GREEN}+{Fore.WHITE}] encrypted_{file} Created...")
    sleep(0.5)
    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done encrypt ..')
