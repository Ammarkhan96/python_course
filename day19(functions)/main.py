# a = 9
# b = 8
# geomean = (a*b)/(a+b)
# print(geomean)

# c = 8
# d = 7
# geomean2 = (c*d)/(c+d)
# print(geomean2)

#FUNCTION

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
 if(a>b):
    print("First number is Greater")
 else:
     print("Second number is Greater or equal")

def isLesser(a, b):
   pass


a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)

c = 8
d = 7
# if(c>d):
#     print("First number is Greater")
# else:
#     print("Second number is Greater or equal")
isGreater(c, d)
calculateGmean(c, d)