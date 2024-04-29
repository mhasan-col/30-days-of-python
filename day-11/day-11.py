# Murtaza
# 4/29/2024
## IMPORTS
import math
import statistics

print('--- Exercises: Level 1  ---\n')
questionCount = 0


# 1.	Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a=1, b=2):
  return a + b


questionCount += 1
print('-- Question {}: '.format(questionCount))
print(add_two_numbers())


# 2.	Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r=10):
  return math.pi * r * r


questionCount += 1
print('-- Question {}: '.format(questionCount))
print(area_of_circle())


# 3.	Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def sum_all_nums(*nums):
  total = 0
  for num in nums:
    if isinstance(num, int):
      total += num
    else:
      print("Arguments need to be on type INT...Breaking...\n")
      break
  return total


questionCount += 1
print('-- Question {}: '.format(questionCount))
print(sum_all_nums(1, 2, 4, 5))


# 4.	Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celcius=10):
  return (celcius * (9 / 5)) + 32


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(convert_celsius_to_fahrenheit(30))


# 5.	Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month="September"):
  autumn = ['September', 'October', 'November']
  winter = ['December', 'January', 'February']
  spring = ['March', 'April', 'May']
  summer = ['June', 'July', 'August']
  if month in autumn: print("The season is Autumn")
  elif month in winter: print("The season is Winter")
  elif month in spring: print("The season is Spring")
  else: print("The season is Summer")


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(check_season())


# 6.	Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(point1=(1, 1), point2=(4, 6)):
  return (point2[1] - point1[1]) / (point2[0] - point1[0])


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(calculate_slope())


# 7.	Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a=1, b=1, c=-30):
  return (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(solve_quadratic_eqn())


# 8.	Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(nums=[1, 2, 3, 4, 5]):
  for i in nums:
    print(i)


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(print_list())


# 9.	Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(nums):
  print(nums[::-1])


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


# 10.	Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(letters=['a', 'b', 'c']):
  return [x.upper() for x in letters]


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(capitalize_list_items())


# 11.	Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list1, object_add):
  list1.append(object_add)
  return list1


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
print(add_item(food_staff, 'Meat'))
print(add_item(numbers, 5))


# 12.	Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list1, object_remove):
  list1.remove(object_remove)
  return list1


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))


# 13.	Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
  total = 0
  for i in range(num + 1):
    total += i
  return total


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# 14.	Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num=10):
  total = 0
  for i in range(num + 1):
    if i % 2: total += i
  return total


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(sum_of_odds())


# 15.	Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num=10):
  total = 0
  for i in range(num + 1):
    if not i % 2: total += i
  return total


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(sum_of_even())

print('\n--- Exercises: Level 2  ---\n')


# 1.	Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(nums=10):
  even, odd = 0, 0
  for i in range(nums + 1):
    if i % 2: odd += 1
    else: even += 1
  return "Evens: {}, Odds: {}".format(even, odd)


questionCount = 1
print('\n-- Question {}: '.format(questionCount))
print(evens_and_odds())


# 2.	Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
  fact = 1
  for num in range(2, n + 1):
    fact *= num
  return fact


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(factorial(10))


# 3.	Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(list1):
  if len(list1): return True
  return False


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(is_empty([]))

# 4.	Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
stat_list = [1, 2, 3, 4, 5, 6]


def calculate_mean(stat_list):
  return sum(stat_list) / len(stat_list)


questionCount += 1
print('\n-- Question {}a: '.format(questionCount))
print(calculate_mean(stat_list))


def calculate_median(stat_list):
  n = len(stat_list)
  s = sorted(stat_list)
  return (s[n // 2 - 1] / 2.0 + s[n // 2] / 2.0,
          s[n // 2])[n % 2] if n else None


print('\n-- Question {}b: '.format(questionCount))
print(calculate_median(stat_list))


def calculate_mode(stat_list):
  return max(set(stat_list), key=stat_list.count)


print('\n-- Question {}c: '.format(questionCount))
print(calculate_mode(stat_list))


def calculate_range(stat_list):
  return "Max: {}, Min: {}".format(max(stat_list), min(stat_list))


print('\n-- Question {}d: '.format(questionCount))
print(calculate_range(stat_list))


def calculate_variance(stat_list):
  return sum(
      (i - calculate_mean(stat_list))**2 for i in stat_list) / len(stat_list)


print('\n-- Question {}e: '.format(questionCount))
print(calculate_variance(stat_list))


def calculate_std(stat_list):
  return statistics.stdev(stat_list)


print('\n-- Question {}f: '.format(questionCount))
print(calculate_std(stat_list))

print('\n--- Exercises: Level 3  ---\n')


# 1.	Write a function called is_prime, which checks if a number is prime.
def is_prime(num=10):
  for i in range(2, (num // 2) + 1):
    # If num is divisible by any number between
    # 2 and n / 2, it is not prime
    if (num % i) == 0:
      print(num, "is not a prime number")
      break
    else:
      print(num, "is a prime number")


questionCount = 1
print('\n-- Question {}: '.format(questionCount))
print(is_prime())


# 2.	Write a functions which checks if all items are unique in the list.
def is_unique(list1=[1, 2, 3, 4, 5, 5]):
  return len(list1) == len(set(list1))


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(is_unique())


# 3.	Write a function which checks if all the items of the list are of the same data type.
def same_type(list1=[1, 2, 3, 4, '5']):
  for i in range(1, len(list1)):
    if type(list1[i - 1]) == type(list1[i]): continue
    else:
      return "NOT THE SAME TYPE OF ITEMS IN LIST"
  return "SAME TYPE OF ITEMS"


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(same_type())


# 4.	Write a function which check if provided variable is a valid python variable
def is_variable(string="variable123"):
  return string.isidentifier()


questionCount += 1
print('\n-- Question {}: '.format(questionCount))
print(is_variable())

# 5.	Go to the data folder and access the countries-data.py file.
from countries_data import *


# •	Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(list1):
  lang = {}
  for i in list1:
    for j in i['languages']:
      if j not in lang:
        lang[j] = 0
      lang[j] += 1
  lang = dict(sorted(lang.items(), key=lambda item: item[1], reverse=True))
  return lang.keys()


questionCount += 1
print('\n-- Question {}a: '.format(questionCount))
print(most_spoken_languages(list1))


# •	Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(list1):
  populate = {}
  for i in list1:
    populate[i['name']] = i['population']
  populate = dict(
      sorted(populate.items(), key=lambda item: item[1], reverse=True))
  return populate.items()


print('\n-- Question {}b: '.format(questionCount))
print(most_populated_countries(list1))
