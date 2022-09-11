from PyPDF2 import PdfFileReader, PdfWriter
import os
import re

RED = "\033[91m"
GREEN = "\033[32m"
RESET = "\033[0m"
 
for pdf_file in os.listdir('pdf'):
    if pdf_file.endswith('.pdf'):
        try:
            pdf = PdfFileReader(f'pdf/{pdf_file}')
            output = PdfWriter()
            for i in range(pdf.getNumPages()):
                current_page = pdf.getPage(i)
                current_page_number = int(re.findall(
                    r'\d+[\s]?[/][\s]?\d+', current_page.extract_text())[-1].split('/')[0])
                try:
                    next_page_number = int(re.findall(
                        r'\d+[\s]?[/][\s]?\d+', pdf.getPage(i+1).extract_text())[-1].split('/')[0])
                except IndexError:
                    next_page_number = -1
                if (next_page_number != current_page_number):
                    output.add_page(current_page)

            with open(f'pdf/{pdf_file}', 'wb') as f:
                output.write(f)
                print(f"{GREEN}[SUCCESS]:{RESET} Successfully formated the file: {pdf_file}")
        except:
            print(f"{RED}[ERROR]:{RESET} Couldn\'t format the file: {pdf_file}")
