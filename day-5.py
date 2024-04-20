# Murtaza
# 4/18/2024


# 1.	Declare an empty list
res = []
# 2.	Declare a list with more than 5 items
res = [0,1,2,3,4,5]
# 3.	Find the length of your list
print("Length of list res is: ", len(res))
# 4.	Get the first item, the middle item and the last item of the list
print("First item is {}, middle item is {}, last item is {}".format(res[0], res[3], res[-1]))
# 5.	Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Murtaza', 18, 173, 'Bare Single', 'Georgia']
# 6.	Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7.	Print the list using print()
for i in it_companies: print(i)
# 8.	Print the number of companies in the list
print("Num of Companies: ", len(it_companies))
# 9.	Print the first, middle and last company
print('First: {}, Middle: {}, Last: {}'.format(it_companies[0], it_companies[3], it_companies[-1]))
# 10.	Print the list after modifying one of the companies
it_companies[0] = 'ColPipe'
for i in it_companies: print(i)
# 11.	Add an IT company to it_companies
it_companies.add('Netflix')
# 12.	Insert an IT company in the middle of the companies list
it_companies.add('RBC', 4)
# 13.	Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
# 14.	Join the it_companies with a string '#;  '

# 15.	Check if a certain company exists in the it_companies list.
# 16.	Sort the list using sort() method
# 17.	Reverse the list in descending order using reverse() method
# 18.	Slice out the first 3 companies from the list
# 19.	Slice out the last 3 companies from the list
# 20.	Slice out the middle IT company or companies from the list
# 21.	Remove the first IT company from the list
# 22.	Remove the middle IT company or companies from the list
# 23.	Remove the last IT company from the list
# 24.	Remove all IT companies from the list
# 25.	Destroy the IT companies list
# 26.	Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# 29.	After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
