import tkinter as tk

def create_GUI(s):
    # Create the main window
    root = tk.Tk()
    root.title("GUI Button Example")

    s.go_to("https://twitter.com/Microsoft")

    def on_closing():
        s.close()
        root.destroy()  # Close the GUI window

    root.protocol("WM_DELETE_WINDOW", on_closing)

    button_function_OP = lambda: s.access_OP_posts(1) # OP posts
    button_function_COMMENTER = lambda: s.access_COMMENTER_posts() # COMMENTER posts
    button_function_EXTRACT = lambda: s.save_data()

    # Create a button widget
    button_OP = tk.Button(root, text="OP Posts", command=button_function_OP)
    button_OP.pack(pady=20)

    button_COMMENTER = tk.Button(root, text="Commenter Posts", command=button_function_COMMENTER)
    button_COMMENTER.pack(pady=20)

    button_EXTRACT = tk.Button(root, text="Extract Data", command=button_function_EXTRACT)
    button_EXTRACT.pack(pady=20)

    # Run the event loop
    root.mainloop()