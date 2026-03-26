# Simple Python Program
# A basic calculator with user input

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def main():
    print("=" * 40)
    print("     Simple Calculator Program")
    print("=" * 40)
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("\nEnter choice (1/2/3/4): ")
        
        if choice == '1':
            print(f"\n{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"\n{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("\nInvalid choice! Please select 1, 2, 3, or 4.")
    
    except ValueError:
        print("\nError: Please enter valid numbers!")

if __name__ == "__main__":
    main()
