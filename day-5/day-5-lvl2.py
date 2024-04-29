# Murtaza
# 4/20/2024

print('--- Question 1 ---\n')
#1.	The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#a.	Sort the list and find the min and max age
ages.sort()
print("Max #: ", ages[-1])
print("Min #: ", ages[0])
#b.	Add the min age and the max age again to the list
ages.insert(0, ages[0])  # Min at the same location so no need to re-sort
ages.append(ages[-1])
#c.	Find the median age (one middle item or two middle items divided by two)
mid = len(ages) // 2
median = (ages[mid] + ages[~mid]) / 2
print("Median is: ", median)
#d.	Find the average age (sum of all items divided by their number )
sum_ages = 0
for i in ages:
  sum_ages += i
print("Average age is: ", sum_ages / len(ages))
#e.	Find the range of the ages (max minus min)
print("The current list: ", ages)
#f.	Compare the value of (min - average) and (max - average), use abs() method
print("Min - Average: ", abs(ages[0] - (sum_ages / len(ages))))
print("Max - Average: ", abs(ages[-1] - (sum_ages / len(ages))))

print('--- Question 2 ---\n')
from countries import *
#1.	Find the middle country(ies) in the countries list
print("Middle Country from List: ", countries[len(countries) // 2])
#2.	Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_1 = countries[:len(countries) // 2 + 1]
countries_2 = countries[len(countries) // 2:] if len(
    countries) % 2 == 0 else countries[len(countries) // 2 + 1:]
print("Last countries_1 element: ", countries_1[-1])
print("First countries_2 element: ", countries_2[0])
#3.	['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = [
    'China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'
]
scandic_countries = []
while countries[-1] != 'USA':
  scandic_countries.append(countries.pop())

print("Countries List: ", countries)
print("Scandic Countries List: ", scandic_countries)
