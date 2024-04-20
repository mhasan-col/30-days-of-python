# Murtaza
# 4/20/2024

print('--- Exercises: Level 1  ---\n')
#1.	Create an empty dictionary called dog
dog = {}
#2.	Add name, color, breed, legs, age to the dog dictionary
dog['name'], dog['color'], dog['breed'], dog['legs'], dog[
    'age'] = "Mark", "Brown", "Husky", 4, 10
#3.	Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Murtz',
    'last_name': 'Hasan',
    'gender': 'Male',
    'age': 25,
    'married': False,
    'skills': ['None', 'Cooking'],
    'country': 'USA',
    'city': 'Alpharetta',
    'address': '1000 Lake St',
}
#4.	Get the length of the student dictionary
print("Length of Student Dictionary: ", len(student))
#5.	Get the value of skills and check the data type, it should be a list
print("Type of skills key in dictionary: ", type(student['skills']))
#6.	Modify the skills values by adding one or two skills
student['skills'].extend(['IDK', 'Bored'])
print("Skills of Dictionary Now: ", student['skills'])
#7.	Get the dictionary keys as a list
print("Keys: ", student.keys())
#8.	Get the dictionary values as a list
print("Values: ", student.values())
#9.	Change the dictionary to a list of tuples using items() method
print("Dictionary to List of Tuples: ", student.items())
print("Type of Dictionary to List of Tuples: ", type(student.items()))
#10.	Delete one of the items in the dictionary
student.pop('married')
#11.	Delete one of the dictionaries
del student
