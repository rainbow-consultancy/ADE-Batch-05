# conditional statements in Python

x = int(input("Enter a number: "))


if x > 2:
    print(x, "is greater then 2")

# ------------------------------------------    

if x > 2:
    print(x, "is greater then 2")
else:
    print(x, "is less then or equals to 2")
    
# ---------------------------------------------

if x > 10:
    print(x, "is greater then 10")
elif x > 5:
    print(x, "is between 6 and 10")
elif x == 5:
    print("Both the numbers are equal -", x)
else:
    print(x, "is less then 5")
    
# ------------------------------------------------

# nested if statements

if x > 5:
    if x <= 10:
        print(x, "is between 5 and 10")
    else:
        print(x, "is greater then 10")
        
# ------------------------------------------

# short - hand notation

result = (x, "is greater then 2") if x > 2 else (x, "is less then or equals to 2")
# print(result)

num_type = "Even" if x % 2 == 0 else "Odd"
print(num_type)

