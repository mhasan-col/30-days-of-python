# Murtaza
# 4/29/2024

## IMPORTS
import string
import random
global questionCount


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(result)
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1


# 1.	Write a function which generates a six digit/character random_user_id.
def random_user_id():
  result = ""
  for i in range(6):
    if random.randint(0, 1):
      result += string.ascii_letters[random.randint(0, 25)]
    else:
      result += str(random.randint(0, 9))
  return result


questionCount = print_output(questionCount, level, random_user_id())


# 2.	Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user(num_char=6, num_ids=5):
  result = []
  temp = ""
  for i in range(num_ids):
    for j in range(num_char):
      if random.randint(0, 1):
        temp += string.ascii_letters[random.randint(0, 25)]
      else:
        temp += str(random.randint(0, 9))
    result.append(temp)
    temp = ""
  return result


questionCount = print_output(questionCount, level, user_id_gen_by_user())


# 3.	Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
  return "rgb({},{},{})".format(random.randint(0, 255), random.randint(0, 255),
                                random.randint(0, 255))


questionCount = print_output(questionCount, level, rgb_color_gen())

print('\n--- Exercises: Level 2  ---\n')
questionCount, level = 0, 2


# 1.	Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num=5):
  hexa = [i for i in range(0, 10)]
  hexa = hexa + ['a', 'b', 'c', 'd', 'e', 'f']
  temp = "#"
  result = []
  for i in range(num):
    for j in range(6):
      temp += str(hexa[random.randint(0, 15)])
    result.append(temp)
    temp = "#"
  return result


questionCount = print_output(questionCount, level, list_of_hexa_colors())


# 2.	Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num=5):
  res = []
  for i in range(num):
    res.append(rgb_color_gen())
  return res


questionCount = print_output(questionCount, level, list_of_rgb_colors())


# 3.	Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color, number):
  if color == 'hexa':
    return list_of_hexa_colors(number)
  elif color == 'rgb':
    return list_of_rgb_colors(number)


questionCount = print_output(questionCount, level, generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

print('\n--- Exercises: Level 3  ---\n')
questionCount, level = 0, 3


# 1.	Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(list1=[1, 2, 3, 4, 5, 6]):
  res = []
  while len(list1):
    res.append(list1[random.randint(0, len(list1) - 1)])
    list1.remove(res[-1])
  return res


questionCount = print_output(questionCount, level, shuffle_list())


# 2.	Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_list():
  nums = [i for i in range(1, 10)]
  res = []
  for i in range(7):
    index = random.randint(0, len(nums) - 1)
    res.append(nums[index])
    nums.remove(res[-1])
  return res


questionCount = print_output(questionCount, level, unique_list())
