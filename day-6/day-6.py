# Murtaza
# 4/20/2024

print('--- Exercises: Level 1  ---\n')
#1.	Create an empty tuple
test_empty = ()
#2.	Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Adnan', 'Justin')
sisters = ('Girl_1', 'Girl_2')
#3.	Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
#4.	How many siblings do you have?
print("I have {} siblings".format(len(siblings)))
#5.	Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Dad', 'Mom')
print('Family Members: ', family_members)

print('--- Exercises: Level 2  ---\n')
#1.	Unpack siblings and parents from family_members
siblings = family_members[:4]
parents = family_members[len(family_members) - 2:]
print("Siblings: ", siblings)
print("Parents: ", parents)
#2.	Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Orange', 'Tomatoes')
vegetables = ('Celery', 'Carrot', 'Broccoli')
animal_products = ('Poop', 'Feathers', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
print(" Tuple food_stuff_tp : ", food_stuff_tp)
#3.	Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)
print("List food_stuff_tp : ", food_stuff_tp)
#4.	Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("Middle Item(s): ", food_stuff_tp[len(food_stuff_tp) // 2])
#5.	Slice out the first three items and the last three items from food_staff_lt list
print("First 3 Items: ", food_stuff_tp[:3])
print("Last 3 Items: ", food_stuff_tp[len(food_stuff_tp) - 3:])
#6.	Delete the food_staff_tp tuple completely
del food_stuff_tp
#7.	Check if an item exists in tuple:
#   •	Check if 'Estonia' is a nordic country
#   •	Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia' in nordic country?: ", 'Estonia' in nordic_countries)
print("Iceland' in nordic country?: ", 'Iceland' in nordic_countries)
