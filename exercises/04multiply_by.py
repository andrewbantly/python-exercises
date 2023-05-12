# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]
num_list = [1, 5, 10, 1239]

result_list = []

def multiply_by(list, num):
    for number in list:
        output = number * num
        result_list.append(output)
    print(result_list)

multiply_by(num_list, 190)



def multiply_by_alt(nums, operator):
    for i in range(len(nums)):
        nums[i] = nums[i] * operator
    
    return nums

print(multiply_by_alt([1, 2, 3], 5))