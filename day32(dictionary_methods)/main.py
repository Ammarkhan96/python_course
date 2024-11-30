# update()

employePerfoemnace1 = {122: 45, 123: 89, 567: 69, 670: 69}
employePerfoemnace2 = {222: 67, 566: 90}
employePerfoemnace1.update(employePerfoemnace2)
print(employePerfoemnace1)


# clear()

employePerfoemnace1 = {122: 45, 123: 89, 567: 69, 670: 69}
employePerfoemnace2 = {222: 67, 566: 90}
employePerfoemnace1.clear()
print(employePerfoemnace1)



# empty()

empt = {}
print(empt)


# pop()

employePerfoemnace1 = {122: 45, 123: 89, 567: 69, 670: 69}
employePerfoemnace2 = {222: 67, 566: 90}
employePerfoemnace1.pop(122)
print(employePerfoemnace1)


# popitem()

employePerfoemnace1 = {122: 45, 123: 89, 567: 69, 670: 69}
employePerfoemnace2 = {222: 67, 566: 90}
employePerfoemnace1.popitem()
print(employePerfoemnace1)


# del()

employePerfoemnace1 = {122: 45, 123: 89, 567: 69, 670: 69}
employePerfoemnace2 = {222: 67, 566: 90}
del employePerfoemnace1[122]
print(employePerfoemnace1)