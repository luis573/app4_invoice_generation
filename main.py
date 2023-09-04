import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths=glob.glob("invoices/*.xlsx") #cria lista com os paths do ficheiros

for filepath in filepaths:
    df=pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf= FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem  #retira só o nome do ficheiro
    invoice_nr, date= filename.split("-") # o invoice recebe o item 0 (10001) da lista e o date o item 1 (2023.1.18)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr. {invoice_nr}",ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50,h=8,txt=f"Date: {date}")







    pdf.output(f"PDFs/{filename}.pdf")