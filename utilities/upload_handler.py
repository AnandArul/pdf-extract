import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pdfplumber

def upload_file(frame):
    file_path=filedialog.askopenfilename(
        title="Select a file",
        filetypes=[('PDF files', '.pdf')]
    )
    if file_path:
        sales_data=[]
        headers=[]

        with pdfplumber.open(file_path) as pdf:
            # sales_data=pdf.pages[0].extract_text()
            # print(sales_data)
            for page in pdf.pages:
                tables=page.extract_tables()
                print(len(tables))
                # if tables:
                #     headers=tables[0][0]
                #     for row in tables[0][1:]:
                #         sales_data.append(row)
                # print(page.extract_text()+'\n')
                # sales_data+=page.extract_text() +'\n'
        # print(sales_data)
        data=tk.Label(frame, text=sales_data, bg='white')
        data.pack()
        
        print(headers)
    
    # # return 'Hello'
    # data=tk.Label(frame,text='Hello',bg='white')
    # data.pack()
    # data.grid(row=3,column=1)
    # print('Hello')
    # # return ''