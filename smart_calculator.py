# Smart Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

while True:
    print("\n--- SMART CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Rectangle Area")
    print("6. Rectangle Perimeter")
    print("0. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "0":
        print("Calculator closed.")
        break
    elif choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            else:
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            
    elif choice in ["5", "6"]:
        try:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            
            if choice == "5":
                print("Area:", rectangle_area(length, width))
            else:
                print("Perimeter:", rectangle_perimeter(length, width))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    else:
        print("Invalid option. Try again.")