# Types of Loops

# 1. for loop  --> this is used when you know how many times you have to repeat something
# 2. while loop  --> this is used when you don't know many iterations it will take to achieve the result


# Examples

# print(1)
# print(2)

for i in range(1, 6):
    print(i)
    
a = ["a", "b", "c", "d", "e"]

for i in a:
    print(i.upper())
    
for i in range(0, len(a)):
    print(a[i])


for i in range(2, 50, 2):
    print(i)

for i in range(2, 50):
    if i%2==0:
        print(i)
        
        
name = "Python"

for i in name:
    print(i)


i = 1

while i <= 5:
    if i == 3:
        i += 1 
        continue
    else:
        print(i)
        i = i + 1
        
while i <= 5:
    if i == 3:
        i += 1 
        break
    else:
        print(i)
        i = i + 1
        
        
# break - will stop the Loop
# continue - will skip the iteration


# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# .
# .
# .
# 2 * 10 = 20


for i in range(1, 11):
    print("2 *", i, "=", 2*i)
    
    
# string formatters

# .format()
# f""


for i in range(1, 11):
    print("2 * {0} = {1}".format(i, 2*i))
    
for i in range(1, 11):
    print(f"2 * {i} = {2*i}")
    

# nested loops

for i in range(2, 10):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    print(50 * "-")


for i in range(1, 6):
    print(i * "*")