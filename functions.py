# methods / functions 

# name = input("Enter Your Name: ")

def greet(name):
    return f"Hey {name}, welcome to this course"

# print(greet("Sandeep"))

# print(greet("Harish"))

# print(greet("Karthik"))

result = greet("Sandeep")
# print(result)


def greet(name):
    print(f"Hey {name}, welcome to this course")
    
# result2 = greet("Lokesh")
# print(result2)


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a/b

def main():
    ops = input(
        """
        Choose the following options:
        1. Add
        2. Sub
        3. Mul
        4. Div
        : """
    )
    input1 = int(input("Please enter the first number: "))
    input2 = int(input("Please enter the second number: "))
    
    if ops == "Add":
        print(add(input1, input2))
    elif ops == "Sub":
        print(sub(input1, input2))
    elif ops == "Mul":
        print(multi(input1, input2))
    elif ops == "Div":
        print(div(input1, input2))
    else:
        print(f"Invalid Operation: please select from the above list")


main()
