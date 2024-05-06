# Murtaza
# 5/2/2024

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

# 1. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
questionCount = print_output(questionCount, level, (), "")
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, rus = names

print("nordic_countries: ", nordic_countries)
print("es: ", es)
print("rus: ", rus)


