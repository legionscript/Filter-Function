"""
Filter Function -> Filters the items in a sequence with a function
that returns True/False for each element
the resulting list will contain only the elements returning true
when passed into the function
"""

def greator_than_5(num):
    return num > 5

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

filtered_list = filter(greator_than_5, numbers)

# print(list(filtered_list))

# def is_even(num):
#     return num % 2 == 0

is_even = filter(lambda num: num % 2 == 0, numbers)

print(list(is_even))