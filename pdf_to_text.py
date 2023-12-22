import fitz  # PyMuPDF
import os
def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text("text")
    doc.close()
    return text
def main():
    #mention the name of your directory containing the pdfs.
    pdf_dir = "docs"
    
    output_file = "docs.txt"
    
    if not os.path.exists(pdf_dir):
        print(f"Directory '{pdf_dir}' does not exist.")
        return
    
    pdf_files = [file for file in os.listdir(pdf_dir) if file.endswith(".pdf")]
    
    with open(output_file, "w", encoding="utf-8") as combined_file:
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_dir, pdf_file)
            text = pdf_to_text(pdf_path)
            combined_file.write(text)

if __name__ == "__main__":
    main()
