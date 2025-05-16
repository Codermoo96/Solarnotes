import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
from datetime import datetime

# Skapa huvudfönstret
root = tk.Tk()
root.title("Solcellsnotis - Viktor")

# Funktion för att skapa och visa rapport
def generera_rapport():
    kundnamn = entry_kundnamn.get().strip()
    if not kundnamn:
        messagebox.showerror("Fel", "Fyll i kundens namn")
        return

    # Hämta data från fälten
    data = {etikett: fält.get() for etikett, fält in entry_fields.items()}
    fritext = fritext_falt.get("1.0", tk.END).strip()

    # Strukturera texten
    rapport = f"""
KUND: {kundnamn}
Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}

*FÖRUTSÄTTNINGAR SOLCELLER*
Taktyp / Material: {data['Taktyp / Material']}
Ålder på tak: {data['Ålder på tak']}
Total årsförbrukning: {data['Total årsforbrukning']}
Taklutning: {data['Taklutning']}
Mark till fot?: {data['Mark till fot?']}
Säker gård?: {data['Säker gård?']}
Organisationsnummer: {data['Orgnr']}
Kabeldimension: {data['Kabeldimension']}
Skuggning: {data['Skuggning?(Träd m.m)']}
Säkring (Amp): {data['Säkring amp']}
Laddbox (Elbil)?: {data['Laddbox?(Elbil)']}
Batteri?: {data['Batteri?']}
Finansiering: {data['Finansiering?']}
Tidslinje: {data['Tidslinje?']}


*FRITEXT*
{fritext}
"""

    # Visa rapporten i rutan
    rapportruta.config(state="normal")
    rapportruta.delete("1.0", tk.END)
    rapportruta.insert(tk.END, rapport.strip())
    rapportruta.config(state="disabled")

    # Spara till fil
    mappnamn = os.path.join("customers", kundnamn.replace(" ", "_"))
    os.makedirs(mappnamn, exist_ok=True)
    with open(os.path.join(mappnamn, "anteckningar.txt"), "w", encoding="utf-8") as f:
        f.write(rapport.strip())

# Layout
etiketter = [
    "Taktyp / Material", "Ålder på tak", "Total årsforbrukning", "Taklutning",
    "Mark till fot?", "Säker gård?", "Orgnr", "Kabeldimension",
    "Skuggning?(Träd m.m)", "Säkring amp", "Laddbox?(Elbil)", "Batteri?"
    , "Finansiering?","Tidslinje?"
]

entry_fields = {}

frame_inputs = tk.Frame(root)
frame_inputs.pack(side=tk.LEFT, padx=10, pady=10)

label_kund = tk.Label(frame_inputs, text="Kundens namn:")
label_kund.grid(row=0, column=0, sticky="w")
entry_kundnamn = tk.Entry(frame_inputs, width=40)
entry_kundnamn.grid(row=0, column=1)

for i, etikett in enumerate(etiketter):
    lbl = tk.Label(frame_inputs, text=etikett + ":")
    lbl.grid(row=i+1, column=0, sticky="w")
    entry = tk.Entry(frame_inputs, width=40)
    entry.grid(row=i+1, column=1)
    entry_fields[etikett] = entry

# Fritextruta
fritext_label = tk.Label(frame_inputs, text="Fritext:")
fritext_label.grid(row=len(etiketter)+2, column=0, sticky="nw")
fritext_falt = scrolledtext.ScrolledText(frame_inputs, width=30, height=10)
fritext_falt.grid(row=len(etiketter)+2, column=1, pady=10)

# Generera-knapp
knapp = tk.Button(root, text="Generera & Spara", command=generera_rapport, bg="lightgreen")
knapp.pack(pady=5)

# Ruta för att visa rapporten
rapportruta = scrolledtext.ScrolledText(root, width=80, height=40, state="disabled", bg="#f5f5f5")
rapportruta.pack(padx=10, pady=10, side=tk.RIGHT)

root.mainloop()