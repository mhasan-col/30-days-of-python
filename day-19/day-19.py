# Murtaza
# 5/3/2024

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

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

questionCount = print_output(questionCount, level, (), "")

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
questionCount = print_output(questionCount, level, (), "")

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
questionCount = print_output(questionCount, level, (), "")

print('\n--- Exercises: Level 2  ---\n')
questionCount, level = 0, 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
questionCount = print_output(questionCount, level, (), "")

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
questionCount = print_output(questionCount, level, (), "")

# 6. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
questionCount = print_output(questionCount, level, (), "")

# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
questionCount = print_output(questionCount, level, (), "")

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
questionCount = print_output(questionCount, level, (), "")

# 9. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
questionCount = print_output(questionCount, level, (), "")
