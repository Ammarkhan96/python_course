# Dictionary

# dic = {
#     "Ammar": "Human Being",
#     "Spoon": "Object"
# }

# print(dic["Ammar"])


# dic = {
#     129332: "Hamid",
#     113444: "Shakir",
#     182384: "Zoha",
#     129982: "Ayesha",
#     173285: "Zakir",
#     157467: "Bismah"
# }

# print(dic[157467])


# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info['name'])
# print(info.get('eligible'))



# How to access all keys and values

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# print(info.keys())
# print(info.values())


# for key in info.keys():
#      print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.item():
    print(f"The value corresponding to the key {key} is {value}")