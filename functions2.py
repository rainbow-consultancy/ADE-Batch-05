def add(a, b, c):
    return a + b + c


# print(add(10, 20))

# print(add(10, 20, 30))

def add(a, b, c=0):
    return a + b + c

# print(add(10, 20))
# print(add(10, 20, 30))


def add(a, b, c=0):
    return a + b + c

# print(add(10, 20))


# -- anonymous functions (lambda functions)

# example

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_evens(li: list) -> list:
    nums = []
    for i in li:
        if i%2 == 0:
            nums.append(i)
    return nums

# print(get_evens(nums))

# lambda function

# even_nums = list(filter(lambda x: x%2 == 0, nums))
# print(even_nums)

is_even = lambda x: x%2 == 0
print(is_even(10))
print(is_even(9))


add = lambda a, b: a + b
print(add(10, 30))


# 1. filter -> is a function which can be used to filter the items based on condition
# 2. map -> map is a function used to apply a functionality/logic to all the items in the iterable object

nums = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x**2, nums))
print(squared_nums)

even_nums = list(map(lambda x: x%2 == 0, nums))
print(even_nums)

even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)

