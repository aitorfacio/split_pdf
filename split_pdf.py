from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from shutil import make_archive

def split_in_files(input_path, output_path, result_file_pages):
    inputpdf = PdfReader(open(input_path, "rb"))
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    n_pages = len(inputpdf.pages)

    splitted_pages = list(range(n_pages))
    splitted_pages = [splitted_pages[n:n+result_file_pages] for n in range(0, len(splitted_pages), result_file_pages)]
    for doc_pages in splitted_pages:
        output = PdfWriter()
        for p in doc_pages:
            output.add_page(inputpdf.pages[p])
        output_document = output_dir / f"splitted_document_pages{'_'.join([str(x+1) for x in doc_pages])}.pdf"
        with open(output_document, 'wb') as output_stream:
            output.write(output_stream)
    output_zip = output_dir.parent /'splitted_pages'
    make_archive(output_zip, 'zip', str(output_dir))

    return f"{output_zip.name}.zip"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    input_file = r'10.03.2023.pdf'
    output_path = 'tmp'

    split_in_files(input_file, output_path, 2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
