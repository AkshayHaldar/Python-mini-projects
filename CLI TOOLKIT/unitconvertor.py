

# Length Conversions --------
def meters_to_kilometers(m):
    return m / 1000

def kilometers_to_meters(km):
    return km * 1000

def meters_to_centimeters(m):
    return m * 100

def centimeters_to_meters(cm):
    return cm / 100


# Weight Conversions --------
def kilograms_to_grams(kg):
    return kg * 1000

def grams_to_kilograms(g):
    return g / 1000


def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Back")

        choice = input("Select option: ")

        if choice == "3":
            return   # back to main menu

        try:
            if choice == "1":
                print("\nLength Converter")
                print("1. Meters → Kilometers")
                print("2. Kilometers → Meters")
                print("3. Meters → Centimeters")
                print("4. Centimeters → Meters")

                option = input("Choose conversion: ")
                value = float(input("Enter value: "))

                if option == "1":
                    print("Result:", meters_to_kilometers(value), "km")
                elif option == "2":
                    print("Result:", kilometers_to_meters(value), "m")
                elif option == "3":
                    print("Result:", meters_to_centimeters(value), "cm")
                elif option == "4":
                    print("Result:", centimeters_to_meters(value), "m")
                else:
                    print("Invalid choice")
            elif choice == "2":
                print("\nWeight Converter")
                print("1. Kilograms → Grams")
                print("2. Grams → Kilograms")

                option = input("Choose conversion: ")
                value = float(input("Enter value: "))

                if option == "1":
                    print("Result:", kilograms_to_grams(value), "g")
                elif option == "2":
                    print("Result:", grams_to_kilograms(value), "kg")
                else:
                    print("Invalid choice")

            else:
                print("Invalid option")

        except ValueError:
            print("Please enter a valid number")
