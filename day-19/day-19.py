# Murtaza
# 5/3/2024

## IMPORTS
global questionCount
from stop_words import *
import os
import json
import string
import re

###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result, text):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(text + ": " + str(result))
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def count_lines_words(filename):
  f = open(filename, 'r')
  lines = f.read().splitlines()
  num_lines = len(lines)

  num_words = 0
  for line in lines:
    num_words += len(line.split(' '))

  return "Number of words: {} and Number of Lines: {} in {}".format(num_words, num_lines, filename.split('/')[-1])

questionCount = print_output(questionCount, level, count_lines_words("./day-19/obama_speech.txt"), "")
print(count_lines_words("./day-19/donald_speech.txt"))
print(count_lines_words("./day-19/melina_trump_speech.txt"))
print(count_lines_words("./day-19/michelle_obama_speech.txt"))

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def top_langs(filename):
  langs = {}
  with open(filename) as f:
    d = json.load(f)
    f.close()
  for i in d:
    for lang in i['languages']:
      if lang not in langs: langs[lang] = 0
      langs[lang] += 1
  langs = sorted(langs.items(), key=lambda x: x[1], reverse=True)
  return langs[:10]

questionCount = print_output(questionCount, level, top_langs('countries_data.json'), "Top languages from countries_data.json are: ")

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def top_countries(filename):
  countries = {}
  with open(filename) as f:
    d = json.load(f)
    f.close()
  for i in d:
    countries[i['name']] = i['population']

  countries = sorted(countries.items(), key = lambda x: x[1], reverse = True)
  return countries[:10]

questionCount = print_output(questionCount, level, top_countries('countries_data.json'), "Top populated countries include: ")

print('\n--- Exercises: Level 2  ---\n')
questionCount, level = 0, 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def email_addresses(filename):
  emails = set()
  with open(filename, "r") as f:
    for line in f:
      if len(line) > 8 and line[:6] == "Author":
        emails.add((line[8:-1]))
  return emails


questionCount = print_output(questionCount, level, email_addresses('email_exchange_big.txt'), "")

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(filename, top_count):
  with open(filename, 'r') as file:
    data = file.read().replace('\n', '')
    data_cleaned = re.sub(r'[!|@|$|%|&|#|;|:|.|?|,|\']', ' ', data).split(' ')
  
  words = {}
  for word in data_cleaned:
    if word == '': continue
    if word not in words: words[word] = 0
    words[word] += 1

  return sorted(words.items(), key = lambda x: x[1], reverse = True)[:top_count]

questionCount = print_output(questionCount, level, find_most_common_words('./day-19/obama_speech.txt', 10), "")

# 6. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech

questionCount = print_output(questionCount, level, find_most_common_words('./day-19/obama_speech.txt', 10), "Obama Speech: ")
print("Michelle Speech: {}".format(find_most_common_words('./day-19/michelle_obama_speech.txt', 10)))
print("Donald Speech: {}".format(find_most_common_words('./day-19/donald_speech.txt', 10)))
print("Melania Speech: {}".format(find_most_common_words('./day-19/melina_trump_speech.txt', 10)))
      
# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
def clean_text(filename):
  with open(filename, 'r') as file:
    data = file.read()
  return re.sub(r'[!|@|$|%|&|#|;|:|.|?|,|\']', ' ', data.replace('\n', ''))

def remove_support_words(data, stop_words):
  stop_words = set(stop_words)
  data = data.split(' ')
  data_1 = []
  for i in range(len(data)):
    if data[i] not in stop_words: data_1.append(data[i])
  return data_1

def check_text_similarity(filename_1, filename_2, stop_words):

  def count_words(data):
    speech_count = {}
    for i in data:
      if i not in speech_count: speech_count[i] = 0
      speech_count[i] += 1
    return sorted(speech_count.items(), key = lambda x: x[1], reverse = True)

  speech_1 = count_words(remove_support_words(clean_text(filename_1), stop_words))
  speech_2 = count_words(remove_support_words(clean_text(filename_2), stop_words))

  print('Speech ' + filename_1 + ': ')
  print(speech_1)
  print('-----------------------------')
  print('Speech ' + filename_2 + ': ')
  print(speech_2)
  

questionCount = print_output(questionCount, level, check_text_similarity('./day-19/donald_speech.txt', './day-19/obama_speech.txt', stop_words), "")

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
questionCount = print_output(questionCount, level, (), "")

# 9. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
questionCount = print_output(questionCount, level, (), "")
