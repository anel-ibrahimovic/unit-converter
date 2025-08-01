def get_menu_choice(prompt, min_option, max_option):
    while True:
        try:
            choice = int(input(prompt))
            if min_option <= choice <= max_option:
                return choice
            else:
                print(f"Enter a number between {min_option} and {max_option}.")
        except ValueError:
            print("Invalid input. Try again.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")

def prompt_return():
    return input("Press 'm' to return to the main menu or any other key to convert again: ").strip().lower() == 'm'

def run_conversion(conversions):
    while True:
        for k, v in conversions.items():
            print(f"{k}. {v[0]}")
        choice = get_menu_choice("Select an option: ", min(conversions), max(conversions))
        label, func, from_unit, to_unit = conversions[choice]
        value = get_float_input(f"Enter value in {from_unit}: ")
        result = func(value)
        print(f"{value} {from_unit} is {result:.2f} {to_unit}.")
        if prompt_return():
            break

def temperature():
    conversions = {
        1: ("Celsius to Fahrenheit", lambda x: (x * 9/5) + 32, "°C", "°F"),
        2: ("Fahrenheit to Celsius", lambda x: (x - 32) * 5/9, "°F", "°C"),
        3: ("Celsius to Kelvin", lambda x: x + 273.15, "°C", "K"),
        4: ("Kelvin to Celsius", lambda x: x - 273.15, "K", "°C"),
        5: ("Fahrenheit to Kelvin", lambda x: (x - 32) * 5/9 + 273.15, "°F", "K"),
        6: ("Kelvin to Fahrenheit", lambda x: (x - 273.15) * 9/5 + 32, "K", "°F")
    }
    run_conversion(conversions)

def length():
    conversions = {
        1: ("Kilometers to Meters", lambda x: x * 1000, "km", "m"),
        2: ("Meters to Kilometers", lambda x: x / 1000, "m", "km"),
        3: ("Meters to Centimeters", lambda x: x * 100, "m", "cm"),
        4: ("Centimeters to Meters", lambda x: x / 100, "cm", "m"),
        5: ("Meters to Millimeters", lambda x: x * 1000, "m", "mm"),
        6: ("Millimeters to Meters", lambda x: x / 1000, "mm", "m"),
        7: ("Meters to Feet", lambda x: x * 3.28084, "m", "ft"),
        8: ("Feet to Meters", lambda x: x / 3.28084, "ft", "m"),
        9: ("Inches to Centimeters", lambda x: x * 2.54, "in", "cm"),
        10: ("Centimeters to Inches", lambda x: x / 2.54, "cm", "in"),
        11: ("Feet to Inches", lambda x: x * 12, "ft", "in"),
        12: ("Inches to Feet", lambda x: x / 12, "in", "ft")
    }
    run_conversion(conversions)

def weight():
    conversions = {
        1: ("Tonnes to Kilograms", lambda x: x * 1000, "t", "kg"),
        2: ("Kilograms to Tonnes", lambda x: x / 1000, "kg", "t"),
        3: ("Kilograms to Grams", lambda x: x * 1000, "kg", "g"),
        4: ("Grams to Kilograms", lambda x: x / 1000, "g", "kg"),
        5: ("Kilograms to Pounds", lambda x: x * 2.20462, "kg", "lbs"),
        6: ("Pounds to Kilograms", lambda x: x / 2.20462, "lbs", "kg"),
        7: ("Grams to Ounces", lambda x: x * 0.035274, "g", "oz"),
        8: ("Ounces to Grams", lambda x: x / 0.035274, "oz", "g"),
        9: ("Pounds to Ounces", lambda x: x * 16, "lbs", "oz"),
        10: ("Ounces to Pounds", lambda x: x / 16, "oz", "lbs")
    }
    run_conversion(conversions)

def main():
    while True:
        print("\nWhat would you like to convert?")
        print("1. Temperature")
        print("2. Length")
        print("3. Weight")
        print("4. Exit")

        choice = get_menu_choice("Select an option (1-4): ", 1, 4)

        if choice == 1:
            temperature()
        elif choice == 2:
            length()
        elif choice == 3:
            weight()
        elif choice == 4:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
