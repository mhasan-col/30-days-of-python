# Murtaza
# 5/13/2024

## IMPORTS
import numpy as np
import statistics as st
from collections import Counter as ct
global questionCount


###### HELPER FUNCTIONS ######
def print_output(questionCount, level, result, text):
  questionCount += 1
  print('\n-- Level {} + Question {}: '.format(level, questionCount))
  print(text + ": " + str(result))
  return questionCount


print('\n--- Exercises: Level 1  ---\n')
questionCount, level = 0, 1


class Statistics:

  def __init__(self, data):
    self.data = data

  def count(self):
    return len(self.data)

  def sum(self):
    return sum(self.data)

  def min(self):
    return min(self.data)

  def max(self):
    return max(self.data)

  def range(self):
    return max(self.data) - min(self.data)

  def mean(self):
    return np.mean(self.data)

  def median(self):
    return np.median(self.data)

  def mode(self):
    mode_value = st.mode(self.data)
    return {'mode': mode_value, 'count': self.data.count(mode_value)}

  def std(self):
    return np.std(self.data)

  def var(self):
    return st.variance(self.data)

  def freq_dist(self):
    return ct(self.data)

questionCount = print_output(questionCount, level, (), "")
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist())

print('\n--- Exercises: Level 2  ---\n')
questionCount, level = 0, 2

class PersonAccount:
  def __init__(self, firstname, lastname, incomes, expenses):
      self.firstname = firstname
      self.lastname = lastname
      self.incomes = incomes
      self.expenses = expenses

  def total_income(self):
      return sum(self.incomes.values())

  def total_expense(self):
      return sum(self.expenses.values())

  def account_info(self):
      return "{} {}'s Account:\nTotal Income: {}, Total Expense: {}\nAccount Balance: {}".format(self.firstname, self.lastname, self.total_income(), self.total_expense(), self.account_balance())
          
  def add_income(self, data):
      for k, val in data.items():
          self.incomes[k] = val
      return dict(sorted(self.incomes.items(), key=lambda x: x[1], reverse=True))

  def add_expense(self, data):
      for k, val in data.items():
          self.expenses[k] = val
      return dict(sorted(self.expenses.items(), key=lambda x: x[1], reverse=True))

  def account_balance(self):
      return self.total_income() - self.total_expense()

account = PersonAccount("Justin", "Johnson")
account.add_income(5000, "IT Work")
account.add_income(100000, "Salary")
account.add_expense(2000, "Groceries")
account.add_expense(500, "Dinner")
print(account.account_info())
      
print('\n--- Exercises: Level 3  ---\n')
questionCount, level = 0, 3
