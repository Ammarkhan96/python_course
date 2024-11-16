# tup = (1,)
# print(type(tup), tup)

# tup = (1, 5, 6)
# print(type(tup), tup)

# tup = (1, 2, 76,89, 9)
# tup[0] = 90
# print(type(tup), tup)

# tup = (3, 8, 67,49, 2, "green", True)
# print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[23])

tup = (1, 2, 76, 342, 32, "blue", True)

if 342 in tup:
    print("Yes 342 is present in this Tuple")


tup2 = tup[1:4]
print(tup2)