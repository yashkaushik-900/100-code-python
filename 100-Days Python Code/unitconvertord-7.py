# 🧮 Unit Converter in Python

def length_converter():
    print("\nLength Converter (Meter, Kilometer, Centimeter, Mile, Foot)")
    meter = float(input("Enter value in meters: "))
    print(f"Kilometers: {meter / 1000}")
    print(f"Centimeters: {meter * 100}")
    print(f"Miles: {meter / 1609.34}")
    print(f"Feet: {meter * 3.28084}")

def weight_converter():
    print("\nWeight Converter (Kilogram, Gram, Pound, Ounce)")
    kg = float(input("Enter value in kilograms: "))
    print(f"Grams: {kg * 1000}")
    print(f"Pounds: {kg * 2.20462}")
    print(f"Ounces: {kg * 35.274}")

def temperature_converter():
    print("\nTemperature Converter (Celsius, Fahrenheit, Kelvin)")
    celsius = float(input("Enter value in Celsius: "))
    print(f"Fahrenheit: {(celsius * 9/5) + 32}")
    print(f"Kelvin: {celsius + 273.15}")

def main():
    while True:
        print("\n===== Unit Converter =====")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
