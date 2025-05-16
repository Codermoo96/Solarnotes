import tkinter as tk
from tkinter import messagebox
import os

# Skapa fönstret
root = tk.Tk()
root.title("SolNotis - Kundanteckningar")

# Skapa funktion för att generera och spara rapport
def generera_rapport():
    # Hämtar värden från fälten
    kundens_namn = entry_namn.get()
    taktyp = entry_taktyp.get()
    alder_tak = entry_alder_tak.get()
    arsforbrukning = entry_arsforbrukning.get()
    taklutning = entry_taklutning.get()
    fritext = text_fritext.get("1.0", tk.END)

    # Kontrollera att kundens namn är ifyllt
    if not kundens_namn:
        messagebox.showerror("Fel", "Kundens namn måste fyllas i.")
        return

    # Skapa mapp om den inte finns
    if not os.path.exists(kundens_namn):
        os.makedirs(kundens_namn)

    # Skapa textinnehåll för rapporten
    rapport = f"""Förutsättningar solceller:
    Taktyp: {taktyp}
    Ålder på tak: {alder_tak}
    Total Årsförbrukning: {arsforbrukning}
    Taklutning: {taklutning}

    Fritext:
    {fritext}
    """

    # Spara texten i en fil
    filepath = os.path.join(kundens_namn, f"{kundens_namn}_rapport.txt")
    with open(filepath, "w") as file:
        file.write(rapport)

    messagebox.showinfo("Framgång", f"Rapport sparad för {kundens_namn}!")

# Skapa GUI-komponenter
label_namn = tk.Label(root, text="Kundens namn:")
label_namn.grid(row=0, column=0, padx=10, pady=5)

entry_namn = tk.Entry(root)
entry_namn.grid(row=0, column=1, padx=10, pady=5)

label_taktyp = tk.Label(root, text="Taktyp:")
label_taktyp.grid(row=1, column=0, padx=10, pady=5)

entry_taktyp = tk.Entry(root)
entry_taktyp.grid(row=1, column=1, padx=10, pady=5)

label_alder_tak = tk.Label(root, text="Ålder på tak:")
label_alder_tak.grid(row=2, column=0, padx=10, pady=5)

entry_alder_tak = tk.Entry(root)
entry_alder_tak.grid(row=2, column=1, padx=10, pady=5)

label_arsforbrukning = tk.Label(root, text="Total Årsförbrukning:")
label_arsforbrukning.grid(row=3, column=0, padx=10, pady=5)

entry_arsforbrukning = tk.Entry(root)
entry_arsforbrukning.grid(row=3, column=1, padx=10, pady=5)

label_taklutning = tk.Label(root, text="Taklutning:")
label_taklutning.grid(row=4, column=0, padx=10, pady=5)

entry_taklutning = tk.Entry(root)
entry_taklutning.grid(row=4, column=1, padx=10, pady=5)

label_fritext = tk.Label(root, text="Fritext:")
label_fritext.grid(row=5, column=0, padx=10, pady=5)

text_fritext = tk.Text(root, height=5, width=40)
text_fritext.grid(row=5, column=1, padx=10, pady=5)

# Generera-knapp
button_generera = tk.Button(root, text="Generera Rapport", command=generera_rapport)
button_generera.grid(row=6, column=0, columnspan=2, pady=10)

# Starta fönstret
root.mainloop()
