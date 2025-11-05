# 🧮 Simple Calculator in Python

def calculator():
    while True:
        print("\n----- Simple Calculator -----")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Average")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        # Exit condition
        if choice == '6':
            print("✅ Exiting Calculator... Goodbye!")
            break

        # Take number inputs
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter numeric values.")
            continue

        # Operations
        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("⚠️ Error: Division by zero is not allowed!")
        elif choice == '5':
            print(f"Average of {num1} and {num2} = {(num1 + num2) / 2}")
        else:
            print("⚠️ Invalid choice! Please select 1-6.")

# Run the calculator
calculator()
# This code provides a simple command-line calculator that can perform basic arithmetic operations and calculate the average of two numbers.