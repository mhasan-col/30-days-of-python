# Murtaza
# 4/22/2024

print('--- Exercises: Level 1  ---\n')
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
print("For Loop:")
for_loop = [print(x) for x in range(11)]
count = 0
while count <= 10: print(count); count += 1
# 2. Iterate 10 to 0 using for loop, do the same using while loop.
print("Reversed For Loop:")
for_loop = [print(x) for x in range(10, -1, -1)]
while count != 0: print(count); count -= 1
# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("-- Q3 --")
count = 1
for i in range(7):
  for i in range(count):
    print("#", end="")
  count += 1
  print("")
# 4. Use nested loops to create the following:
print("-- Q4 --")
for i in range(8):
  for j in range(8):
    print("#", end=" ")
  print("")
# 5. Print the following pattern:
print("-- Q5 --")
for i in range(11):
  print("{} x {} = {}".format(i, i, i * i))
# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
tech = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in tech: print(i)
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
print(" Even #s ")
for i in range(101):
  if not i % 2: print(i, end=" ")

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
print("\n Odd #s ")
for i in range(101):
  if i % 2: print(i, end=" ")
    
print('--- Exercises: Level 2  ---\n')
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
count = 0
for i in range(101):
  count += i
print("Sum of all Numbers: ", count)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even, odd = 0, 0
for i in range(101):
  if not i % 2: even += i
  else: odd += i

print("Sum of Even: {}, Sum of Odd: {}".format(even, odd))

print('--- Exercises: Level 3  ---\n')
from countries import *
from countries_data import *
from collections import Counter
# 1.	Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for i in countries: 
  if 'land' in i: print(i)
# 2.	This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit = []
for i in reversed(fruit):
  reversed_fruit.append(i)
print("Reversed Fruit List: ", reversed_fruit)

# 3.	Go to the data folder and use the countries_data.py file.

    # - What are the total number of languages in the data
language_count = 0
languages = []
population = {}
for i in list1:
  language_count += len(i['languages'])
  languages += i['languages']
  population[i['name']] = i['population']


print("Length of all languages: ", language_count)
    # - Find the ten most spoken languages from the data
data = Counter(languages)
print("The Top languages are: ", data.most_common(10))
    # - Find the 10 most populated countries in the world
res = dict(sorted(population.items(), key=lambda x: x[1], reverse=True)[:10])
print("Top 10 most populated countries in the world: ", res)