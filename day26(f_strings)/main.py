# letter = "Hey my name is {} and I am from {}"
# country="Pakisatan"
# name="Ammar"

# print(letter.format(name, country))



#But when I will give formate like this (country, name)

letter = "Hey my name is {1} and I am from {0}"
country="Pakisatan"
name="Ammar"

print(letter.format(country, name))

#After f-string

letter = "Hey my name is {} and I am from {}"
country="Pakisatan"
name="Ammar"

print(f"Hey my name is {name} and I am from {country}")



# txt = "For only {price:.2f} dollars!"

# print(txt.format(price = 49.09999))


# After f-string
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)


print(type(f"{2 * 30}"))


#if I want currly braces look as it is

letter = "Hey my name is {} and I am from {}"
country="Pakisatan"
name="Ammar"

print(f"We use f-string like this: Hey my name is {{name}} and I am from {{country}}")
