import tkinter as tk
from tkinter import ttk, messagebox

conversion_categories = {
    "Temperature": {
        "Celsius to Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9,
        "Celsius to Kelvin": lambda x: x + 273.15,
        "Kelvin to Celsius": lambda x: x - 273.15,
        "Fahrenheit to Kelvin": lambda x: (x - 32) * 5/9 + 273.15,
        "Kelvin to Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32,
    },
    "Length": {
        "Kilometers to Meters": lambda x: x * 1000,
        "Meters to Kilometers": lambda x: x / 1000,
        "Meters to Centimeters": lambda x: x * 100,
        "Centimeters to Meters": lambda x: x / 100,
        "Meters to Millimeters": lambda x: x * 1000,
        "Millimeters to Meters": lambda x: x / 1000,
        "Meters to Feet": lambda x: x * 3.28084,
        "Feet to Meters": lambda x: x / 3.28084,
        "Inches to Centimeters": lambda x: x * 2.54,
        "Centimeters to Inches": lambda x: x / 2.54,
        "Feet to Inches": lambda x: x * 12,
        "Inches to Feet": lambda x: x / 12,
    },
    "Weight": {
        "Tonnes to Kilograms": lambda x: x * 1000,
        "Kilograms to Tonnes": lambda x: x / 1000,
        "Kilograms to Grams": lambda x: x * 1000,
        "Grams to Kilograms": lambda x: x / 1000,
        "Kilograms to Pounds": lambda x: x * 2.20462,
        "Pounds to Kilograms": lambda x: x / 2.20462,
        "Grams to Ounces": lambda x: x * 0.035274,
        "Ounces to Grams": lambda x: x / 0.035274,
        "Pounds to Ounces": lambda x: x * 16,
        "Ounces to Pounds": lambda x: x / 16,
    }
}

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.category_var = tk.StringVar()
        self.conversion_var = tk.StringVar()
        self.input_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Select Category:").pack(pady=10)
        category_menu = ttk.Combobox(self.root, textvariable=self.category_var, state="readonly")
        category_menu["values"] = list(conversion_categories.keys())
        category_menu.bind("<<ComboboxSelected>>", self.update_conversions)
        category_menu.pack()

        ttk.Label(self.root, text="Select Conversion:").pack(pady=10)
        self.conversion_menu = ttk.Combobox(self.root, textvariable=self.conversion_var, state="readonly")
        self.conversion_menu.pack()

        ttk.Label(self.root, text="Enter Value:").pack(pady=10)
        ttk.Entry(self.root, textvariable=self.input_var).pack()

        ttk.Button(self.root, text="Convert", command=self.convert).pack(pady=10)

        ttk.Label(self.root, text="Result:").pack(pady=5)
        ttk.Label(self.root, textvariable=self.result_var, font=("Arial", 14, "bold")).pack()

    def update_conversions(self, event):
        category = self.category_var.get()
        if category in conversion_categories:
            conversions = list(conversion_categories[category].keys())
            self.conversion_menu["values"] = conversions
            self.conversion_menu.set('')

    def convert(self):
        try:
            value = float(self.input_var.get())
            conversion = self.conversion_var.get()
            category = self.category_var.get()

            if category in conversion_categories and conversion in conversion_categories[category]:
                result = conversion_categories[category][conversion](value)
                self.result_var.set(f"{value} → {result:.2f}")
            else:
                messagebox.showerror("Error", "Invalid conversion selection.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
