import PyPDF2
import pandas as pd
import io
import openpyxl


# specify input pdf file path
input_path = "input_file.pdf"

# specify output excel file path
output_path = "output_file.xlsx"

# read pdf file and store as a bytearray
with open(input_path, 'rb') as pdf_file:
    pdf_data = pdf_file.read()

# create file object from byte array
pdf_file_obj = io.BytesIO(pdf_data)

# create pdf reader object
pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

# iterate through each page and extract text
table = ""
for page in range(len(pdf_reader.pages)):
    table += pdf_reader.pages[page].extract_text() + "\n"

# convert extracted text into a Pandas DataFrame
df = pd.read_csv(io.StringIO(table), sep="\t")

# save the DataFrame as an Excel file
df.to_excel(output_path, index=False)
