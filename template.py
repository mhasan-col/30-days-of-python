# Murtaza
# 4/29/2024

## IMPORTS
global questionCount


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result, text):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(text + ": " + str(result))
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1

questionCount = print_output(questionCount, level, (), "")

print('\n--- Exercises: Level 2  ---\n')
questionCount, level = 0, 2

print('\n--- Exercises: Level 3  ---\n')
questionCount, level = 0, 3
