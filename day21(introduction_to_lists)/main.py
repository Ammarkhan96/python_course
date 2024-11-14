# List 

#simple list
# l = [3, 5, 7]
# print(l)
# print(type(l))


# marks = [3, 5, 7]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

# negative indexes

#to convet negative index into positive
# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])



# marks = [3, 5, 6, "Ammar", True]
# Now if I want to know if an 'element' is present in the list or not

# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# if "Ammar" in marks:
#     print("Yes")
# else:
#     print("No")

# if "amm" in "Ammar":
#     print("Yes")

# if i want print all elements
# print(marks[:])


lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)