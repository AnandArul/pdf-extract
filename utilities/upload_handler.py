import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pdfplumber
import threading

def extract_table_data(file):
    headers=[]
    rows=[]
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            tables=page.extract_tables()
            
            for table in tables:
                if not table:
                    continue
                if not headers:
                    headers=table[0]
                    
                data = table[1:] if table[0] == headers else table
                rows.extend(data)
    return headers,rows

def upload_file(frame, footer_frame):
    sales_value=0
    file_path=filedialog.askopenfilename(
        title="Select a file",
        filetypes=[('PDF files', '.pdf')]
    )
    if not file_path:
        return
    
    headers, rows=extract_table_data(file_path)
    
    if not headers or not rows:
        messagebox.showinfo("No Table Found", "No table data found in the selected PDF.")
        return

    tree=ttk.Treeview(frame)
    tree.pack(side='left',fill='both',expand=True)
    
    # Clear previous data
    for item in tree.get_children():
        tree.delete(item)
    
    tree['columns']=headers
    tree['show']='headings'
    
    for col in headers:
        tree.heading(col,text=col)
        tree.column(col, width=100, anchor='center')
        
    for row in rows:
        sales_value+=float(row[6])
        tree.insert("",'end',values=row)
    
    sb=ttk.Scrollbar(frame,orient='vertical', command=tree.yview)
    sb.pack(side='right',fill='y')
    tree.configure(yscrollcommand=sb.set)
    
    # footer data
    s_count_label=tk.Label(footer_frame, text="Sales Count: ", bg='white', font=('Arial', 15, 'bold'), width=25, anchor='w')
    s_count_label.grid(row=0, column=0)
    
    s_count_value=tk.Label(footer_frame, text=len(rows), bg='white', font=('Arial', 15, 'bold'), width=25, anchor='w')
    s_count_value.grid(row=0,column=1)
    
    t_sales_label=tk.Label(footer_frame, text="Sales Value:", bg='white', font=('Arial', 15, 'bold'), width=25, anchor='w')
    t_sales_label.grid(row=1, column=0)
    
    t_sales_value=tk.Label(footer_frame, text=f'{sales_value:.2f}', bg='white', font=('Arial', 15, 'bold'), width=25, anchor='w')
    t_sales_value.grid(row=1, column=1)