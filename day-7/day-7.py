# Murtaza
# 4/20/2024

print('--- Exercises: Level 1  ---\n')
it_companies = {
    'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1.	Find the length of the set it_companies
print("Length of it_companies: ", len(it_companies))
#2.	Add 'Twitter' to it_companies
it_companies.add('Twitter')
#3.	Insert multiple IT companies at once to the set it_companies
it_companies.update(['Netflix', 'Robinhood', 'Citadel'])
#4.	Remove one of the companies from the set it_companies
it_companies.pop()
#5.	What is the difference between remove and discard
"""
remove(): Will raise an exception/error if item to be removed doesn't exist
discard(): Doesn't care. Will remove if it exists otherwise nothing will change
"""
print('--- Exercises: Level 2  ---\n')
#1.	Join A and B
joined_ab = A.union(B)
#2.	Find A intersection B
intersection_ab = A.intersection(B)
#3.	Is A subset of B
print("Is A subset of B: ", B.issubset(A))
#4.	Are A and B disjoint sets
print("Are A and B disjoint sets?: ", A.isdisjoint(B))
#5.	Join A with B and B with A
join_ab = A.union(B)
join_ba = B.union(A)
print("Join A + B: ", join_ab)
print("Join B + A: ", join_ba)
#6.	What is the symmetric difference between A and B
print("Symmetric difference between A and B: ", A.symmetric_difference(B))
#7.	Delete the sets completely
del A
del B

print('--- Exercises: Level 3  ---\n')
#1.	Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Length of List: ", len(age))
print("Length of Set: ", len(age_set))
#2.	Explain the difference between the following data types: string, list, tuple and set
"""
String: Mutable and Iterable (Changeable and can iterate through)
List: Collections (not exactly) of same format of contents making it Mutable and Iterable
Tuple: Immutable (not changeable) but iterable
Set: Denoted by (), it's the same as list but cannot contain duplicates and sorted by default. Useful b/c look up time is O(1)
"""
#3.	I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
teacher_string = "I am a teacher and I love to inspire and teach people"
print("Unique words set includes: ", len(set(teacher_string.split(' '))))
