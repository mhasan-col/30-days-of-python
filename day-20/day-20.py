# Murtaza
# 5/12/2024

## IMPORTS
import requests
import numpy
from collections import Counter
global questionCount


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result, text):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(text + ": " + str(result))
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
questionCount = print_output(questionCount, level, print("URL Errored with 404"), "")

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
cat_url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cat_url).json()
# 2.1 the min, max, mean, median, standard deviation of cats' weight in metric units.
def get_metrics_array(data):
  minimum = numpy.amin(data)
  maximum = numpy.amax(data)
  mean = numpy.mean(data)
  median = numpy.median(data)
  std = numpy.std(data)
  return 'Min: {}, Max: {}\nMean: {}, Median: {}\nStandard Deviation: {}'.format(minimum, maximum, mean, median, std)

def get_weight(response):
  metric_weights = []
  for breed in response:
    avg_weight = breed['weight']['metric'].split(' - ')
    metric_weights.append((int(avg_weight[0]) + int(avg_weight[-1]))/2)
  
  return get_metrics_array(metric_weights)

questionCount = print_output(questionCount, level, get_weight(response), " Cats' weight in metrics: ")
# 2.2 the min, max, mean, median, standard deviation of cats' lifespan in years.
def get_lifespan(response):
  lifespan = []
  for breed in response:
    avg_lifespan = breed['life_span'].split(' - ')
    lifespan.append((int(avg_lifespan[0]) + int(avg_lifespan[-1]))/2)

  return get_metrics_array(lifespan)

print("Cats' Lifespan: " + get_lifespan(response))

# 2.3 Create a frequency table of country and breed of cats
def sort_dict(data):
  return sorted(data.items(), key=lambda x: x[1], reverse=True)

def country_cats(response):
  country = {}
  for breed in response:
    if breed['origin'] not in country: country[breed['origin']] = 0
    country[breed['origin']] += 1
  return sort_dict(country)

print("Frequency Counter Cats: ", dict(country_cats(response)))

# 3. Read the countries API and find
country_url = 'https://restcountries.com/v3.1/all'
response = requests.get(country_url).json()

# 3.1 the 10 largest countries
def largest_country(response):
  countries = {}
  for country in response:
    countries[country['name']['common']] = country['population']
  return dict(sort_dict(countries)[:10])
questionCount = print_output(questionCount, level, largest_country(response), " 10 Largest Countries: ")

# 3.2 the 10 most spoken languages
def lang_country(response):
  languages = {}
  for country in response:
    for lang in country['languages'].values():
      if lang not in languages: languages[lang] = 0
      languages[lang] += 1
  return sort_dict(languages)
  
print("Most spoken languages: ", dict(lang_country(response)[:10]))

# 3.3 the total number of languages in the countries API
def count_languages(data):
  return len(data.items())

print("Count of total languages: {}".format(count_languages(lang_country(response))))

# 4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
questionCount = print_output(questionCount, level, print("URL Errored with 404"), "")
