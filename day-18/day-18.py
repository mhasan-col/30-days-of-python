# Murtaza
# 5/3/2024

## IMPORTS
import re
global questionCount


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result, text):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(text + ": " + str(result))
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1

# 1. What is the most frequent word in the following paragraph?
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
res = set()
for i in paragraph.split(' '):
  res.add((len(re.findall(i, paragraph)), i))


questionCount = print_output(questionCount, level, res, "")


# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

points_txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction"

nums = [int(i) for i in re.findall(r'-?\d+\b', points_txt)]
questionCount = print_output(questionCount, level, nums[-1] - nums[0], "Distance from furthest points: ")


print('\n--- Exercises: Level 2  ---\n')
questionCount, level = 0, 2

# 1. Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(string):
  if re.findall(r'^\d|(-)', string):
    return False
  return True


questionCount = print_output(questionCount, level, is_valid_variable('first_name'), "Expected True: ")
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True



print('\n--- Exercises: Level 3  ---\n')
questionCount, level = 0, 3

# 1. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
sentence_cleaned = re.sub(r'[!|@|$|%|&|#|;|.|?|,]', '', sentence)

res = {}
for i in sentence_cleaned.split(" "):
  if i not in res: res[i] = 0
  res[i] += 1

questionCount = print_output(questionCount, level, res, "")