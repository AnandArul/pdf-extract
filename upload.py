import tkinter as tk
from tkinter import ttk
from utilities.upload_handler import upload_file



def create_main_window():
    root=tk.Tk()
    root.title('Extract PDF')
    root.attributes('-fullscreen', True)
    
    root.grid_rowconfigure(0, weight=0)
    root.grid_columnconfigure(0, weight=1)
    
    # --------- Style Configuration for White Button ---------
    # style = ttk.Style()
    # style.theme_use('default')  # Use default theme for better styling control

    # style.configure("White.TButton",
    #     background="white",
    #     foreground="black",
    #     borderwidth=1,
    #     padding=6,
    #     font=('Arial', 10, 'bold'),
    #     relief="solid"
    # )
    # style.map("White.TButton",
    #     background=[('active', '#f0f0f0')],
    #     relief=[('pressed', 'sunken'), ('!pressed', 'solid')],
    #     bordercolor=[('!active', '#e1e1e1'), ('active', '#999')]
    # )

    
    # --------title frame config--------
    header_frame=tk.Frame(root,bg='white', borderwidth=1, height=50, padx=10, pady=10, relief='ridge')
    header_frame.grid(row=1, column=0,sticky="ew")
    header_frame.grid_columnconfigure(0, weight=1)
    header_frame.grid_propagate(False)              # sets fixed height
    
    # --------configure titles inside frame--------
    header_label=tk.Label(header_frame, text="Extract Pdf Data", bg='white', font=('Arial', 18, 'bold'))
    header_label.grid(row=0, column=0, sticky="w")
    # header_label.pack(anchor='center')      #center alignment option 1
    # header_label.pack(expand=True)      #center alignment option 2
    
    # --------configure close button inside frame--------
    close_button=tk.Button(header_frame, text="Close", command=root.destroy, bg='white', relief='solid', highlightbackground="#e1e1e1", highlightthickness=1)
    close_button.grid(row=0, column=1, sticky="e")
    
    # --------- ttk.Button on Right ---------
    # header_frame.grid_columnconfigure(0, weight=1)
    # header_frame.grid_columnconfigure(1, weight=0)
    # close_button = ttk.Button(
    #     header_frame,
    #     text="Close",
    #     style="White.TButton",
    #     command=root.destroy
    # )
    # close_button.grid(row=0, column=1, sticky="e", padx=10)
    
    
    # --------configure frame for upload button--------
    upload_frame=tk.Frame(root,bg='white', borderwidth=1, padx=10, pady=20, relief='ridge')
    upload_frame.grid(row=2,column=0,sticky='ew')
    header_frame.grid_columnconfigure(0, weight=1)
    # header_frame.grid_propagate(False)              # sets fixed height
    
    # --------configure upload button inside frame--------
    upload_button=tk.Button(upload_frame, text='Upload', command=lambda:upload_file(data_frame,footer_frame))
    upload_button.grid(row=1,column=1, sticky="ew")
    
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
