import glob
from fpdf import FPDF
from pathlib import Path

filepaths= glob.glob("files_student/*.txt")



pdf=FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()

    filename=Path(filepath).stem #get the filename without extension
    title=filename.capitalize()
    print(title)

    pdf.set_font(family="Arial", style="B",size=20)
    pdf.cell(w=50,h=20,txt=title,ln=1)

    #get content of the txt file
    with open(filepath,"r") as file:
        content=file.read()
    #add the text file to pdf
    pdf.set_font(family="Arial", size=14)
    pdf.multi_cell(w=0, h=8, txt=content)

pdf.output(f"files_student/Animais.pdf")

