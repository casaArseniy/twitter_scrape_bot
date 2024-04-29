import tkinter as tk
from tkinter import messagebox
import csv
from scrapper_classes.scrapper import Scrapper
from credentials import ID, PASSWORD


def main_menu_GUI():
    window = tk.Tk()
    window.title("Menu")
    window.geometry("300x450")
    window.minsize(300, 450)

    # Show all Twitter targets
    def load_csv_data():
        try:
            with open('twitter_scrape_bot/target_data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    listbox.insert(tk.END, f"{row[0]}, {row[1]}")
        except FileNotFoundError:
            listbox.insert(tk.END, f"Name: , URL: ")
    
    # Delete a target from list
    def delete_selected_row():
        selected_index = listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            listbox.delete(index)
            
            # Remove the selected row from the CSV file
            with open('twitter_scrape_bot/target_data.csv', 'r') as file:
                lines = file.readlines()
            with open('twitter_scrape_bot/target_data.csv', 'w') as file:
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
    listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Configure scrollbar to work with Listbox
    scrollbar.config(command=listbox.yview)

    # Load CSV target data
    load_csv_data()

    def input_press_behaviour():
        window.destroy()
        add_target_GUI()
    
    def start_press_behaviour():
        window.destroy()
        control_scrapper_GUI()


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

    window.mainloop()

# Control scrapper manually
def control_scrapper_GUI():
    window = tk.Tk()
    window.title("Test Scrapping")
    window.geometry("450x450")
    window.minsize(300, 200)

    s = Scrapper()


    def on_closing():
        s.close()
        window.destroy()  # Close the GUI window
        main_menu_GUI()
    
    def on_start():
        s.login(ID, PASSWORD)
        s.scrape(target_list, 1)


    window.protocol("WM_DELETE_WINDOW", on_closing)

    target_list = ["https://twitter.com/Microsoft"] 

    # def start_press_behaviour():

    button_function_START = lambda: on_start
    button_START = tk.Button(window, text="START", command=button_function_START)
    button_START.pack(pady=20)

    back_button = tk.Button(window, text="Back", command=on_closing)
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
            with open('twitter_scrape_bot/target_data.csv', 'a', newline='') as file:
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
    submit_button = tk.Button(window, text="Submit", command=button_function_SUBMIT)
    submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(window, text="Back", command=on_closing)
    back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

# input_GUI()