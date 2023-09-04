import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")  # cria lista com os paths do ficheiros

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem  # retira só o nome do ficheiro
    invoice_nr, date = filename.split("-")  # o invoice recebe o item 0 (10001) da lista e o date o item 1 (2023.1.18)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add a header
    columns = df.columns  # obter o nome dos headers no ficheiro excell e conveter em lista
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Arial", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    # tem que se converter para string senão dá erro porque os dados são int
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=50, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], ln=1, border=1)

    # add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Arial", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]),
                 border=1)  # tem que se converter para string senão dá erro porque os dados são int
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), ln=1, border=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Arial", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="")
    pdf.cell(w=50, h=8, txt="")
    pdf.cell(w=50, h=8, txt="")
    pdf.cell(w=30, h=8, txt="Total", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), ln=1, border=1)

    # add sum sentence
    pdf.set_font(family="Arial", size=10, style="B")
    pdf.cell(w=0, h=8, txt=f"The total price is {total_sum}", ln=1)

    # add company name and logo
    pdf.set_font(family="Arial", size=10)
    pdf.cell(w=50, h=8, txt=f"Loja do Mestre Andre")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")
