#strings are immutable

a = "Ammar"
print(len(a))

#upper method
print(a.upper())

#lower method
print(a.lower())

#rstrip method
b = "Hello !!!!!!"
print(b.rstrip("!"))

c = "!!!Hey!!!"
print(c.rstrip("!"))

#replace method
print(a.replace("Ammar", "Ammar Khan"))

#split method
d = "abcd efgh ijkl"
print(d.split(" "))

#capitalized method
blogHeading = "introduction of python"
print(blogHeading.capitalize())

helloWorld = "heLlo worlD"
print(helloWorld.capitalize())

#center method
str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))

#count method
e = "!!!Ammar  !!!!  Ammar!!!"
print(e.count("Ammar"))

#endswith method
str2 = "Welcome to the World!!!"
print(str2.endswith("!!!"))

str2 = "Welcome to the Worlds!!!"
print(str2.endswith("to", 4, 10 ))

str3 = "He's name is Dan. He is honest man."
print(str3.find("is"))
print(str3.find("ishh"))

#index method
# print(str3.index("ishh"))


#isalnum
str4 = "WelcomeToTheConsole"
print(str4.isalnum())

str5 = "Welcom"
print(str5.isalpha())

str6 = "Welcome03"
print(str6.isalpha())

#islower method
str7 = "hello world"
print(str7.islower())

#isprintable method
str8 = "Happy Birthday"
print(str8.isprintable())

#isspace method
str9 = "         "
print(str9.isspace())

#istitle method
str10 = "World Health Organization"
print(str10.istitle())

st11 = "to Kill a mocking bird"
print(st11.istitle())

#isupper method
str12 = "WORLD HEALTH ORGANIZATION"
print(str12.isupper())

#startswith method
str13 = "Python is a Interpretted Programming Language"
print(str13.startswith("Python"))

#swapcase method
str14 = "HELLO"
print(str14.swapcase())

str14 = "world"
print(str14.swapcase())

str15 = "His name is Dan. he is honest man."
print(str15.title())