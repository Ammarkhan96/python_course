num = 18
if(num < 0):
    print("Number is negative.")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")


num = 65
if(num < 2):
    print("Number is negative.")
elif(num > 4):
    if(num <= 20):
        print("Number is between 1-10")
    elif(num > 14 and num <= 30):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")