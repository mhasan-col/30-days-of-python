# Murtaza
# 5/2/2024

## IMPORTS
global questionCount
from datetime import datetime, timedelta


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result, text):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(text + ": " + str(result))
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
time_stamp = datetime.now()
questionCount = print_output(
    questionCount, level,
    ("Datetime Now: {}, Day: {}, Month: {}, Year: {}, Hour: {}, Minute: {}".
     format(time_stamp, time_stamp.day, time_stamp.month, time_stamp.year,
            time_stamp.hour, time_stamp.minute)), "")

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
questionCount = print_output(questionCount, level,
                             time_stamp.strftime("%m/%d/%Y, %H:%M:%S"), "")

# 3. Today is 5 December, 2019. Change this time string to time.
questionCount = print_output(
    questionCount, level, datetime.strptime("5 December, 2019", "%d %B, %Y"),
    "")

# 4. Calculate the time difference between now and new year.
questionCount = print_output(questionCount, level,
                             datetime(2025, 1, 1, 0, 0, 0, 0) - datetime.now(),
                             "time difference between now and new year")

# 5. Calculate the time difference between 1 January 1970 and now.
questionCount = print_output(questionCount, level,
                             datetime.now() - datetime(1970, 1, 1, 0, 0, 0, 0),
                             "time difference between 1 January 1970 and now")

# 6. Think, what can you use the datetime module for? Examples:
#    o	Time series analysis
questionCount = print_output(questionCount, level, (), "")

#    o	To get a timestamp of any activities in an application
questionCount = print_output(questionCount, level, (), "")

#    o	Adding posts on a blog
questionCount = print_output(questionCount, level, (), "")
