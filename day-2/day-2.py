# Murtaza
# 4/16/2024

# Imports
import math

# Exercise 1
## Day 2: 30 Days of python programming
firstname = "Murtaza"
lastname = "Hasan"
fullname = firstname + lastname
country = "United States"
city = "Alpharetta"
age = 24
year = 2024
is_married = False # I wish
is_true = True
is_light_on = True
justin_name, adnan_name = "Justin", "Adnan"

# Exercise 2
variables = [firstname, lastname, fullname, country, city, age, year, is_married, is_true, is_light_on, justin_name, adnan_name]
for i in variables:
    print("Type of variable {} is: {}".format(str(i), type(i)))

# Q2-3
print("Length of first name is: ", len(firstname))
print("Length of last name is: ", len(lastname))
print("Difference of length of first/last name is: ", len(firstname)-len(lastname))

# Q4
num_one, num_two = 4, 5
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = float(num_one) / float(num_two)
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Q5
radius = 30
area_circle = lambda a : math.pi * pow(int(a), 2)
area_circle_system = area_circle(radius)
circum_of_circle = 2 * math.pi * radius

user_radius = input("Provide a custom circle radius value ie. '30': ")
area_circle_user = area_circle(user_radius)

# Q6
firstname = input("Provide a value for your first name: ")
lastname = input("Provide a value for your last name: ")
country = input("Provide a value for your country: ")
age = input("Provide a value for your age: ")

# Q7
help('keywords')