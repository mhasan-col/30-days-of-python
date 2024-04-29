# Murtaza
# 4/29/2024

## IMPORTS
global questionCount


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(result)
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [i for i in numbers if i < 0]
questionCount = print_output(questionCount, level, numbers)

# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_of_lists = [number for row in list_of_lists for sub_row in row for number in sub_row]
questionCount = print_output(questionCount, level, list_of_lists)

# 3. Using list comprehension create the following list of tuples:
list1 = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
questionCount = print_output(questionCount, level, list1)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [country for row in countries for country_1 in row for country in country_1]
questionCount = print_output(questionCount, level, countries)

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [{country_final} for row in countries for country in row for country_final in country]
questionCount = print_output(questionCount, level, countries)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [name[0] + " " + name[1] for array in names for name in array]
questionCount = print_output(questionCount, level, names)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda point1, point2 : (point2[1] - point1[1])/(point2[0] - point1[0])
questionCount = print_output(questionCount, level, slope((5,5),(1,3)))






