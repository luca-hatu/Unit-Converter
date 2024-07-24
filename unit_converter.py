import tkinter as tk
from tkinter import ttk, messagebox
import pint

def fetch_units():
    ureg = pint.UnitRegistry()
    units = [str(unit) for unit in ureg]
    return units

def get_compatible_units(unit):
    ureg = pint.UnitRegistry()
    try:
        input_quantity = ureg(unit)
        base_unit = input_quantity.dimensionality
        compatible_units = [str(u) for u in ureg if ureg(u).dimensionality == base_unit]
        return compatible_units
    except Exception as e:
        print(f"Error fetching compatible units: {e}")
        return []

def convert_units(value, from_unit, to_unit):
    ureg = pint.UnitRegistry()
    from_quantity = value * ureg(from_unit)
    to_quantity = from_quantity.to(ureg(to_unit))
    return to_quantity.magnitude

def update_compatible_units(event):
    from_unit = from_unit_var.get().strip().lower()
    compatible_units = get_compatible_units(from_unit)
    to_unit_var.set('')
    to_unit_combobox['values'] = compatible_units

def perform_conversion():
    try:
        value = float(value_entry.get())
        from_unit = from_unit_var.get().strip().lower()
        to_unit = to_unit_var.get().strip().lower()
        
        if from_unit and to_unit:
            result = convert_units(value, from_unit, to_unit)
            result_label.config(text=f"{value} {from_unit} = {result} {to_unit}")
        else:
            messagebox.showerror("Error", "Please select valid units.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to perform conversion: {e}")


units = fetch_units()

root = tk.Tk()
root.title("Unit Converter")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Value:").grid(row=0, column=0, sticky=tk.W)
value_entry = ttk.Entry(mainframe, width=10)
value_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="From unit:").grid(row=1, column=0, sticky=tk.W)
from_unit_var = tk.StringVar()
from_unit_combobox = ttk.Combobox(mainframe, textvariable=from_unit_var)
from_unit_combobox['values'] = units
from_unit_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E))
from_unit_combobox.bind('<<ComboboxSelected>>', update_compatible_units)

ttk.Label(mainframe, text="To unit:").grid(row=2, column=0, sticky=tk.W)
to_unit_var = tk.StringVar()
to_unit_combobox = ttk.Combobox(mainframe, textvariable=to_unit_var)
to_unit_combobox.grid(row=2, column=1, sticky=(tk.W, tk.E))

convert_button = ttk.Button(mainframe, text="Convert", command=perform_conversion)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = ttk.Label(mainframe, text="")
result_label.grid(row=4, column=0, columnspan=2)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()




