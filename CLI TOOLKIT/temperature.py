

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15


def temperature_converter():
    while True:
        print("\nTemperature Converter")
        print("1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Celsius → Kelvin")
        print("4. Back")

        choice = input("Select option: ")

        if choice == "4":
            return 

        try:
            value = float(input("Enter temperature value: "))

            if choice == "1":
                print("Result:", celsius_to_fahrenheit(value), "°F")
            elif choice == "2":
                print("Result:", fahrenheit_to_celsius(value), "°C")
            elif choice == "3":
                print("Result:", celsius_to_kelvin(value), "K")
            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter a valid number")
