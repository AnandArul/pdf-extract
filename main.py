from tkinter import *
from tkinter import ttk
root=Tk()

root.title('First Python App')
root.attributes('-fullscreen',True)
root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))

try:
    root.state('zoomed')
except:
    screen_width:root.winfo_screenwidth()
    screen_height:root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

print(root.winfo_screenwidth())

form=ttk.Frame(root, padding=100)
form.grid()

ttk.Label(form, text="Extract PDF", font='Arial 18 bold').grid(column=0, row=0)

ttk.Button(form, text="Quit", command=root.destroy).grid(column=0, row=1)

root.mainloop()


# import pdfplumber

# def extract_text_from_pdf(file_path):
#     with pdfplumber.open(file_path) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     return text

# if __name__ == "__main__":
#     pdf_path = "samples/Maersk-rate-sheet.pdf"
#     extracted_text = extract_text_from_pdf(pdf_path)
#     print(extracted_text)
