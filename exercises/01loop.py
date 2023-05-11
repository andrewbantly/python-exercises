# Write a function called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example function call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there


def p_times(statement, num):
    i = 0
    while i < num:
        print(statement)
        i += 1


def a_times(statement, num):
    for _ in range(num):
        print(statement)

p_times("hey Andrew", 4)
a_times("hey murphy", 5)


# range w/ three args (start num = 0, end num, step = 1)
# range with two args (start num, end num) ... step is assumed one
# range with one arg (end num) ... start num assumed = 0, step assumed = 1

for i in range(-10, 10): 
    print(i)