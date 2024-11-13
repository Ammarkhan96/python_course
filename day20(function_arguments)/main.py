# 1. Required Arguments
# def average(a, b):
#     print("The average is", (a+b)/2)

# average(4, 6)


# 2. Default Arguments

# def average(a=9, b=1):
#     print("The average is", (a+b)/2)

# average()
# But if I will give function average to other arguments then it will ignore first values and accept second values
# If i just want to give value b in average
# average(b=9)


# 3. Keyword Arguments:

# def average(a=9, b=1):
#     print("The average is", (a+b)/2)
# average(b=9)
# average(b=9, a=21)



# 4. Required Argument
# def average(a, b=1):
#     print("The average is", (a+b)/2)
# average(a = 21)


# def average(a, b, c = 1):
#     print("The average is", (a+b+c)/2)
# average(5, 6)






# Variable length arguments

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum/len(numbers))
# average(5, 6)


def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname= "Buchanan", lname = "Barnes", fname = "James")