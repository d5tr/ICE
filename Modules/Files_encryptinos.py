from PyPDF2 import PdfFileWriter , PdfFileReader
from time import sleep
import py_compile
from colorama import Fore

class Files_Encryptions :

    def __init__(self, file):

        self.file = file

    def py_encrypt(self):
        
        py_compile.compile(self.file)
        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done encrypt file ..')


    def pdf_encrypt (self, password):
        
        # write in file
        parser = PdfFileWriter()
        
        # read the file
        pdf = PdfFileReader(self.file)
        
        for page in range(pdf.numPages):
            parser.addPage(pdf.getPage(page))
        
        # set password
        parser.encrypt(password)
        
        with open(f"encrypt_{self.file}", "wb") as f:
            parser.write(f)
            f.close()
        print(f"[{Fore.GREEN}+{Fore.WHITE}] encrypted_{self.file} Created...")
        sleep(0.5)
        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done encrypt ..')
