import tkinter as tk
from tkinter import ttk

data = [
    {"name": "John Doe", "email": "john@example.com", "phone": "1234567890"},
    {"name": "Jane Smith", "email": "jane@example.com", "phone": "9876543210"}
]

def print_table():
    root=tk.Tk()
    root.title('Table sample')
    root.attributes('-fullscreen', True)
    l_title=tk.Label(root, text="Print Table")
    l_title.pack()
    
    columns=("name", "email", "phone")
    
    tree=ttk.Treeview(root,columns=columns, show='headings')
    
    # Define headings
    tree.heading("name", text="Name")
    tree.heading("email", text="Email")
    tree.heading("phone", text="Phone")
    
    # Define columns
    tree.column('name', width=100)
    tree.column('email')
    tree.column('phone')
    
    #insert data to tree
    for row in data:
        tree.insert('','end',values=(row['name'], row['email'], row['phone']))
    
    tree.pack(expand=True, fill='both')
    print('Table')
    
    root.mainloop()
    


if __name__=='__main__':
    print_table()