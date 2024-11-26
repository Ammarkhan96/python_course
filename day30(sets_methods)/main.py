# Union (combine both sets)
# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1, s2)



# cities1 = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities1.union(cities2)
# print(cities3)




# Intersection:
# cities1 = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokoyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities1.intersection(cities2)
# cities3 = cities1.intersection(cities2)
# print(cities3)

# cities1 = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokoyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities1.intersection(cities2)
# cities1.intersection_update(cities2)
# print(cities3)




# Symmetric Difference:(It means 'a' intersection 'b', means all the values which are not common)

# cities1 = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokoyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)

# cities1 = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokoyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities1.difference(cities2)
# print(cities3)





# idisjoint: This method checks if items of given set are present in another set.

# cities1 = {"Tokoyo2", "Madrid3", "Berlin", "Delhi"}
# cities2 = {"Tokoyo", "Seoul", "Kabul", "Madrid"}
# print(cities1.isdisjoint(cities2))



# issuperset:
# cities1 = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities1.issuperset(cities2))
# cities3 = {"Tokoyo", "Madrid", "Delhi"}
# print(cities1.issuperset(cities3))
# print(cities3.issubset(cities1))


# cities = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# cities = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokoyo")
# print(cities)

# cities = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# cities.discard("Tokoyo3")
# print(cities)


# cities = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)


# cities = {"Tokoyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)




info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")