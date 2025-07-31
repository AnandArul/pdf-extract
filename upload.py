import tkinter as tk
from tkinter import ttk, PhotoImage
from utilities.upload_handler import upload_file

def create_main_window():
    root=tk.Tk()
    root.title('Extract PDF')
    root.attributes('-fullscreen', True)
    
    root.grid_rowconfigure(0, weight=0)
    root.grid_columnconfigure(0, weight=1)
    
    # --------title frame config--------
    header_frame=tk.Frame(root,bg='white', borderwidth=1, height=50, padx=10, pady=10, relief='ridge')
    header_frame.grid(row=1, column=0,sticky="ew")
    header_frame.grid_columnconfigure(0, weight=1)
    header_frame.grid_propagate(False)              # sets fixed height
    
    # --------configure titles inside frame--------
    header_label=tk.Label(header_frame, text="Extract Pdf Data", bg='white', font=('Arial', 18, 'bold'))
    header_label.grid(row=0, column=0, sticky="w")
    
    # --------configure close button inside frame--------
    close_button=tk.Button(header_frame, 
                   text="Close", 
                   command=root.destroy,
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   highlightbackground="white",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised")
    close_button.grid(row=0, column=1, sticky="e")
    
    # --------configure frame for upload button--------
    upload_frame=tk.Frame(root,bg='white', borderwidth=1, padx=10, pady=20, relief='ridge')
    upload_frame.grid(row=2,column=0,sticky='ew')
    header_frame.grid_columnconfigure(0, weight=1)
    # header_frame.grid_propagate(False)              # sets fixed height
    
    # --------configure upload button inside frame--------
    upload_button=tk.Button(
        upload_frame,
        text="Upload File",
        command=lambda:upload_file(data_frame,footer_frame),
        bg="#0078D7",
        fg="black",
        highlightbackground="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        padx=10,
        pady=5
    )
    upload_button.pack()
    
    upload_desc=tk.Label(upload_frame, text="(upload pdf files only)", bg='white', font=('Arial', 10, 'italic'))
    upload_desc.pack()
    
    # --------configure frame for extracted data--------
    root.grid_rowconfigure(3, weight=1)
    data_frame=tk.Frame(root, bg='white', borderwidth=1, height=300, padx=20, pady=20, relief='ridge')
    data_frame.grid(row=3,column=0, sticky='nsew')
    
    # --------footer data--------
    footer_frame=tk.Frame(root, bg='white', padx=10, pady=10, relief='ridge')
    footer_frame.grid(row=4,column=0, sticky='ew')
    
    root.mainloop()


if __name__=='__main__':
    create_main_window()
