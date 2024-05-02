# Murtaza
# 4/30/2024

## IMPORTS
global questionCount
#from functional import seq
from functools import reduce


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result, text):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(text + ": " + str(result))
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.	Explain the difference between map, filter, and reduce.
questionCount = print_output(questionCount, level, (), "")
print(
    "Map is: takes a lamdba function and iterable (like list) and applies the lambda function to all the values/objects in the iterable\n"
)
print(
    "Filter is: Takes a function that needs to return True/False against an iterable. It will return the items in the iterable that returned True\n"
)
print(
    "Reduce is: takes in a function that has two parameters and an iterable. Runs the function against the iterable to return a single value.\n"
)

# 2.	Explain the difference between higher order function, closure and decorator
questionCount = print_output(questionCount, level, (), "")
print("HOF: Takes a function as an argument or returns a function\n")
print(
    "Closure: An idea where you have a function within a function. Inner function has access to variables in the outer function\n"
)
print(
    "Decorator: Wrap a function with another function with some added functionality\n"
)

# 3.	Define a call function before map, filter or reduce, see examples.
questionCount = print_output(questionCount, level, (), "")

# 4.	Use for loop to print each country in the countries list.
questionCount = print_output(questionCount, level, [i for i in countries], "")

# 5.	Use for to print each name in the names list.
questionCount = print_output(questionCount, level, [i for i in names], "")

# 6.	Use for to print each number in the numbers list.
questionCount = print_output(questionCount, level, [i for i in numbers], "")

print('\n--- Exercises: Level 2  ---\n')
questionCount, level = 0, 2


# 1.	Use map to create a new list by changing each country to uppercase in the countries list
def uppercase_list(x):
  return x.upper()


countries_upper = map(uppercase_list, countries)
questionCount = print_output(questionCount, level, list(countries_upper), "")


# 2.	Use map to create a new list by changing each number to its square in the numbers list
def square_list(x):
  return x**2


numbers_square = map(square_list, numbers)
questionCount = print_output(questionCount, level, list(numbers_square), "")

# 3.	Use map to change each name to uppercase in the names list
names_uppercase = map(uppercase_list, names)
questionCount = print_output(questionCount, level, list(names_uppercase), "")


# 4.	Use filter to filter out countries containing 'land'.
def contains_land(x):
  if 'land' in x: return True
  return False


countries_land = filter(contains_land, countries)
questionCount = print_output(questionCount, level, list(countries_land), "")

# 5.	Use filter to filter out countries having exactly six characters.
countries_six = filter((lambda x: len(x) == 6), countries)
questionCount = print_output(questionCount, level, list(countries_six), "")

# 6.	Use filter to filter out countries containing six letters and more in the country list.
countries_six = filter((lambda x: len(x) >= 6), countries)
questionCount = print_output(questionCount, level, list(countries_six), "")

# 7.	Use filter to filter out countries starting with an 'E'
countries_chain = filter((lambda x: x[0] == 'E'), countries)
questionCount = print_output(questionCount, level, list(countries_chain), "")

# 8.	Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
numbers_chained = filter(lambda x: x >= 2, map(square_list, numbers))
questionCount = print_output(questionCount, level, list(numbers_chained), "")

# 9.	Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
get_string_lists = filter(lambda x: isinstance(x, str), [1, 2, 4, '5', '6'])
questionCount = print_output(questionCount, level, list(get_string_lists), "")


# 10.	Use reduce to sum all the numbers in the numbers list.
def num_sum(x, y):
  return x + y


numbers_sum = reduce(num_sum, numbers)
questionCount = print_output(questionCount, level, list(numbers_sum), "")

# 11.	Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries_cat = reduce(lambda x, y: str(x) + ', ' + str(y),
                       countries) + ' are north european countries'
questionCount = print_output(questionCount, level, list(countries_cat), "")

# 12.	Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import *


def common_pattern(x):
  if 'land' in x or 'ia' in x or 'island' in x or 'stan' in x: return True
  return False


categorize_countries = filter(common_pattern, countries)
questionCount = print_output(questionCount, level, categorize_countries, "")


# 13.	Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def list_to_dict(countries):
  myDict = {}
  for i in countries:
    myDict[i[0]] = i
  return myDict


questionCount = print_output(questionCount, level, list_to_dict(countries), "")


# 14.	Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries):
  return countries[:10]


questionCount = print_output(questionCount, level,
                             get_first_ten_countries(countries), "")


# 15.	Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries):
  return countries[-1:-11:-1]


questionCount = print_output(questionCount, level,
                             get_last_ten_countries(countries), "")

print('\n--- Exercises: Level 3  ---\n')
questionCount, level = 0, 3

# 1.	Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
from countries_data import list1
# o	Sort countries by name, by capital, by population
questionCount = print_output(questionCount, level,
                             sorted(list1, key=lambda x: x['name'])[:10],
                             "Sorted by Name: ")
questionCount = print_output(questionCount, level,
                             sorted(list1, key=lambda x: x['capital'])[:10],
                             "Sorted by Capital: ")
questionCount = print_output(questionCount, level,
                             sorted(list1, key=lambda x: x['population'])[:10],
                             "Sorted by Population: ")

# o	Sort out the ten most spoken languages by location.
# o	Sort out the ten most populated countries.
