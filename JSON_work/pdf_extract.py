
#this is a good way to look at the pdf components


from pdfminer.high_level import extract_pages, extract_text

for page_layout in extract_pages("750 firestorm 2.pdf"):
    for element in page_layout:
        element.extract_text()
        print(element)
