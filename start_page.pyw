import os
import tkinter as tk
from tkinter import messagebox

# Ladda alla kunder från customers-mappen
def load_customers():
    customers = []
    for customer_folder in os.listdir("customers"):
        if os.path.isdir(os.path.join("customers", customer_folder)):
            customers.append(customer_folder.replace("_", " "))  # Återställ mellanslag i kundnamnet
    return customers

# Läs kundens anteckningar från anteckningar.txt
def read_customer_notes(customer_name):
    customer_folder = os.path.join("customers", customer_name.replace(" ", "_"))
    notes_file = os.path.join(customer_folder, "anteckningar.txt")
    
    try:
        with open(notes_file, "r", encoding="utf-8") as f:
            notes = f.read()
    except FileNotFoundError:
        notes = "Ingen anteckning finns för denna kund."
    
    return notes

# Visa kundens anteckningar när man klickar på en kund
def view_customer_notes(customer_name):
    notes = read_customer_notes(customer_name)
    text_notes.delete(1.0, tk.END)  # Rensa tidigare anteckningar i textfältet
    text_notes.insert(tk.END, notes)  # Sätt in kundens anteckningar i textfältet

# Skapa huvudfönstret för CRM
root = tk.Tk()
root.title("CRM System - Kundhantering")
root.geometry("600x400")

# Kundlista
label_customers = tk.Label(root, text="Kundlista:")
label_customers.pack(pady=5)

frame_customers = tk.Frame(root)
frame_customers.pack(pady=10)

# Ladda och visa alla kunder
customers = load_customers()
for customer in customers:
    customer_button = tk.Button(frame_customers, text=customer, width=40, anchor="w", command=lambda c=customer: view_customer_notes(c))
    customer_button.pack(pady=2)

# Textfält för att visa kundens anteckningar
label_notes = tk.Label(root, text="Kundens anteckningar:")
label_notes.pack(pady=5)

text_notes = tk.Text(root, width=70, height=10)
text_notes.pack(pady=10)

root.mainloop()