import tkinter as tk
from tkinter import ttk # Good practice for modern widgets

def create_main_window():
    root = tk.Tk()
    root.title("My Application") # Window title
    

    # Set a minimum size for the window (optional but good for initial view)
    root.attributes('-fullscreen',True)
    # root.geometry("600x400")

    # --- Configure the grid for the main window ---
    # This is important for making the 'title_row_frame' expand and center
    root.grid_rowconfigure(0, weight=0)  # Row 0 (for title) doesn't need to expand vertically
    root.grid_rowconfigure(1, weight=1)  # Subsequent rows can expand vertically (e.g., for content)
    root.grid_columnconfigure(0, weight=1) # Make the single column expand horizontally

    # --- Create a Frame for the Title Row ---
    # This frame will hold the title label and give it a visual border
    title_row_frame = tk.Frame(root,
                               bg="white",           # Background color of the frame
                               borderwidth=1,            # Thickness of the border
                               relief="flat")          # Style of the border (flat, sunken, raised, groove, ridge)

    # Place the title_row_frame in the first row (row=0) and make it span the entire width
    title_row_frame.grid(row=0, column=0, columnspan=1, sticky="nsew", padx=10, pady=10) # padx/pady for spacing around the frame

    # --- Configure the grid INSIDE the title_row_frame for the Label ---
    # This is crucial for centering the label within its parent frame
    title_row_frame.grid_rowconfigure(0, weight=1)    # Allows the label to vertically center if the frame has extra height
    title_row_frame.grid_columnconfigure(0, weight=1) # Allows the label to horizontally center

    # --- Create the Title Label ---
    title_label = tk.Label(title_row_frame,
                            text="My Application Title",
                            font=("Helvetica", 24, "bold"), # Example font
                            bg="lightgray",                 # Match background of the frame
                            fg="darkblue")                  # Text color

    # Place the title_label inside the title_row_frame
    # sticky="nsew" makes the label expand to fill its cell (which is the entire frame in this case)
    # This, combined with grid_columnconfigure(weight=1) on the frame, ensures centering.
    title_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=5) # padx/pady for internal spacing for the label text


    # --- Add some placeholder content in another row ---
    content_label = tk.Label(root, text="This is the main content area.", font=("Arial", 12), bg="lightblue")
    content_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


    root.mainloop()

# Run the function to create the window
if __name__ == "__main__":
    create_main_window()