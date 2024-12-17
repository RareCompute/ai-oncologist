import gradio as gr
from PyPDF2 import PdfReader

def pdf_to_fasta(pdf_file):
    if pdf_file is None:
        return None
    reader = PdfReader(pdf_file.name)
    fasta_content = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        # Process the text to convert it to FASTA format
        # This is a placeholder, you need to implement the actual conversion logic
        fasta_content += f">Page_{i}\n{text}\n"
    
    fasta_file = "output.fasta"
    with open(fasta_file, "w") as f:
        f.write(fasta_content)
    
    return fasta_file

with gr.Blocks() as demo:
    pdf_input = gr.File(label="Upload PDF", type="filepath")
    fasta_output = gr.File(label="Download FASTA")
    
    # Automatically convert when a file is selected
    pdf_input.change(fn=pdf_to_fasta, inputs=pdf_input, outputs=fasta_output)

if __name__ == "__main__":
    demo.launch()