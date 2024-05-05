import tkinter as tk
from tkinter import messagebox
import csv
from resources.scrapper_classes.scrapper import Scrapper
from resources.credentials import ID, PASSWORD
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import datetime
import threading



def main_menu_GUI():
    window = tk.Tk()
    # im = Image.open('mri.jpeg')
    # photo = ImageTk.PhotoImage(im)
    # window.iconphoto(True, photo)
    window.title("Menu")
    # window.geometry("300x650")
    window.minsize(300, 450)

    # Show all Twitter targets
    def load_csv_data():
        try:
            with open('resources/target_data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    listbox.insert(tk.END, f"{row[0]}, {row[1]}")
        except FileNotFoundError:
            listbox.insert(tk.END, f"Name: , URL: ")
    
    def get_single_target():
        # Get the index of the selected item
        selected_index = listbox.curselection()
        # If an item is selected, get its text
        if selected_index:
            index = int(selected_index[0])
            selected_text = listbox.get(index)
            
            # Split the text using comma as separator and get the second part
            return [selected_text.split(',')[1].strip()]
        else:
            messagebox.showwarning("Warning", "Please select a target.")
    
    def get_all_targets():
        target_list = []
        try:
            with open('resources/target_data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    target_list += [row[1]]
        except FileNotFoundError:
            messagebox.showwarning("Warning", "target_data.csv file is missing.")
        
        if len(target_list)==0:
            messagebox.showwarning("Warning", "target_data.csv file is empty, add a target.")
        return target_list

    
    # Delete a target from list
    def delete_selected_row():
        selected_index = listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            listbox.delete(index)
            
            # Remove the selected row from the CSV file
            with open('resources/target_data.csv', 'r') as file:
                lines = file.readlines()
            with open('resources/target_data.csv', 'w') as file:
                writer = csv.writer(file)
                for i, line in enumerate(lines):
                    if i != index:
                        writer.writerow(line.strip().split(','))

        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    # Create a scrollbar
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a Listbox to display target list
    listbox = tk.Listbox(window, yscrollcommand=scrollbar.set, height=10, selectmode='multiple')
    listbox.pack(fill=tk.BOTH, expand=True)

    # Configure scrollbar to work with Listbox
    scrollbar.config(command=listbox.yview)

    # Load CSV target data
    load_csv_data()

    def input_press_behaviour():
        window.destroy()
        add_target_GUI()
    
    def start_press_behaviour():
        target_list = []
        if var.get():
            target_list = get_all_targets()
        else:
            target_list = get_single_target()
        
        if target_list:
            window.destroy()
            control_scrapper_GUI(target_list)

    label = tk.Label(window, text="You can select a single target from list \n or you can select all targets. \n You can also add a target of your choice.")

    # Pack the Label widget into the window
    label.pack(pady=20)

    # Add target manually button
    button_ADD_TARGET = tk.Button(window, text="Add target to list", command=input_press_behaviour)
    button_ADD_TARGET.pack(pady=20)

    # Delete a target manually
    delete_button = tk.Button(window, text="Delete Selected Row", command=delete_selected_row)
    delete_button.pack(pady=10)

    # Start scrapping targets from Twitter
    button_function_scrapping = lambda: start_press_behaviour() 
    button_START = tk.Button(window, text="Start scrapping", command=button_function_scrapping)
    button_START.pack(pady=20)

    # Create a Checkbutton widget for selecting all targets
    var = tk.BooleanVar()
    check_button = tk.Checkbutton(window, text="Select ALL targets", variable=var)
    check_button.pack(pady=20)

    window.mainloop()

# Control scrapper manually
def control_scrapper_GUI(target_list):
    window = tk.Tk()
    window.title("Test Scrapping")
    window.geometry("450x450")
    window.minsize(300, 200)

    s = Scrapper()
    # d = Scrapper()


    def on_closing():
        window.destroy()  # Close the GUI window
        main_menu_GUI()

    
    def start_scraping(driver, selected_date_str):
        driver.start_driver()
        driver.scrape(target_list, selected_date_str, ID, PASSWORD)
    
    def on_start(s):
        try:
            selected_date = cal.selection_get()
            selected_date_str = selected_date.strftime("%Y-%m-%d")

            current_date = datetime.now().date()  # Convert to date object
            current_date_str = current_date.strftime("%Y-%m-%d")

            if selected_date_str > current_date_str:
                messagebox.showerror("Error", "Date is out of range.")
            else:
                thread1 = threading.Thread(target=start_scraping, args = (s, selected_date_str))
                # thread2 = threading.Thread(target=start_scraping, args = (d, selected_date_str))
                thread1.start()
                # thread2.start()
                thread1.join()
                # thread2.join()
        except ValueError:
            messagebox.showerror("Date is out of range.")

    window.protocol("WM_DELETE_WINDOW", on_closing)

    label = tk.Label(window, text="Select a date until which you want to get target posts.")

    # Pack the Label widget into the window
    label.pack(pady=20)

    # Create a Calendar widget for date selection
    cal = Calendar(window, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(padx=10, pady=10)

    button_function_START = lambda: on_start(s)
    button_START = tk.Button(window, text="START", command=button_function_START)
    button_START.pack(pady=20)

    back_button = tk.Button(window, text="BACK", command=on_closing)
    back_button.pack(pady=20)

    # Run the event loop
    window.mainloop()

def add_target_GUI():
    # Create GUI window
    window = tk.Tk()
    window.title("Add to CSV")
    window.geometry("300x200")
    window.minsize(300, 200)

    def on_closing():
        window.destroy()  # Close the GUI window
        main_menu_GUI()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    def add_to_csv(name_entry, url_entry):
        name = name_entry.get()
        url = url_entry.get()
        
        if name.strip() == '' or url.strip() == '':
            messagebox.showerror("Error", "Please enter both Name and URL")
        else:
            with open('resources/target_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, url])
                messagebox.showinfo("Success", "Data added to CSV successfully")

    # Name label and entry
    name_label = tk.Label(window, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    # URL label and entry
    url_label = tk.Label(window, text="URL:")
    url_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
    url_entry = tk.Entry(window)
    url_entry.grid(row=1, column=1, padx=10, pady=5)

    # Submit button
    def submit_press_behaviour(name_entry, url_entry):
        add_to_csv(name_entry, url_entry)
        window.destroy()
        main_menu_GUI()
    
    button_function_SUBMIT = lambda: submit_press_behaviour(name_entry, url_entry)

    #button_function_submit = lambda: add_to_csv(name_entry, url_entry)
    submit_button = tk.Button(window, text="SUBMIT", command=button_function_SUBMIT)
    submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(window, text="BACK", command=on_closing)
    back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

# input_GUI()