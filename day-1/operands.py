## Murtaza
## 4/15/2024

## Q1. Python Version
import sys
import platform
print("Python Details: {}".format(sys.version))

## Q2. Operations
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

## Q3. Strings
name = "Murtaza"
family = "Hasan"
country ="Canada"
print(name)
print(family)
print(country)
print("I'm not enjoying 30 days of python")

## Q4. Data Types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(family))
print(type(country))

# Exercise 3
## Q1
print(type(False))
print(type([0,1,2,3,4]))
print(type((1,2,3)))
print(type(set([0,0,1,2,3])))
print(type({'a': 0, 'b': 1, 'c': 2}))

## Q2. Euclidian Distance
point1 = [2, 3]
point2 = [10, 8]

import math
distance = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
print("Distance between {},{} & {},{} is: {}".format(point1[0], point1[1], point2[0], point2[1], distance))
