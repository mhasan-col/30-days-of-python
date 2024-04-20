# Murtaza
# 4/20/2024

print('--- Exercises: Level 1  ---\n')
#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
user_age = int(input("Enter your age...: "))
if user_age > 18: print("You are old enough to drive.")
else: print("Wait for the missing amount of years")
#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 25
if user_age > my_age:
  print("You're a grandpa by {} years".format(user_age - my_age))
elif user_age < my_age:
  print("You're baby by {} years".format(my_age - user_age))
else:
  print("We're in the same hell")
#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
(a, b) = input("Enter two numbers seperated by comma: ").split()
if a > b: print("A is greater than B")
elif b > a: print("B is greater than A")
else: print("They're the same")

print('\n--- Exercises: Level 2  ---\n')
#1. Write a code which gives grade to students according to theirs score
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""


def letterGrade(grade):
  if (grade >= 80): return "A"
  elif (70 <= grade < 90): return "B"
  elif (60 <= grade < 70): return "C"
  elif (50 <= grade < 60): return "D"
  else: return "F"


print("Percent to Letter Grade is: ",
      letterGrade(int(input("Enter a pecent: "))))

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter month in its full form eg. September...: ")
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
if month in autumn: print("The season is Autumn")
elif month in winter: print("The season is Winter")
elif month in spring: print("The season is Spring")
else: print("The season is Summer")

#3. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter a fruit...: ")
if user_fruit not in fruits:
  fruits.append(user_fruit)
  print("Added {} to the fruits list".format(user_fruit))
else:
  print("That fruit already exist in the list")

print('--- Exercises: Level 3  ---\n')
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
  print("Middle of skills list: ",
        person['skills'][len(person['skills']) // 2])
#2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
  print("Is Python in list?: ", 'Python' in person['skills'])
#3. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if all(x in person['skills'] for x in ['React', 'Node', 'MongoDB']):
  print('He is a fullstack developer')
if all(x in person['skills'] for x in ['Node', 'Python', 'MongoDB']):
  print('He is a backend developer')
if all(x in person['skills'] for x in ['JavaScript', 'React']):
  print('He is a front end developer')
else:
  print('Unknown Title')
#4. If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] and person['country'] == 'Finland':
  print("{} {} lives in {}. He is married".format(person['first_name'],
                                                  person['last_name'],
                                                  person['country']))
