import fitz
def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    
    # Initialize a dictionary to hold the text from each page
    pdf_text = {}
    
    # Iterate over each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        page_text = page.get_text()
        
        # Store the text of the page in the dictionary
        pdf_text[page_num + 1] = page_text
    
    return pdf_text


