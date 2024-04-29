# Murtaza
# 4/17/2024

# Q1
print("Thirty " + "days " + "Of " + "Python")
print("Coding" + " " + "For" + " " + "All")
company = "Coding For All"
print(company)
print("Length of company variable is: ", len(company))
print("lowercase 'murtaza' becomes: ", 'murtaza'.upper())
print("uppercase 'MURTAZA' becomes: ", 'murtaza'.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print("Sliced string: ", company[7:])
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
print('Python for Everyone'.replace('Everyone', 'All'))
print(company.split(' '))
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))
print('Character at index 0 is: ', company[0])
print('Last Character is: ', company[-1])
print('Character at index 10 is: ', company[10])

# Q18 - inf
PFE = "Python For Everyone"
print('Acroynm is: {}{}{}'.format(PFE[0], PFE[7], PFE[11]))
print('Acroynm is: {}{}{}'.format(company[0], company[7], company[11]))

# Q20
print("Index for C is: ", company.index('C'))
print("Index for F is: ", company.index('F'))
print("rFind for l is: ", 'Coding For All People'.rfind('l'))

because_string = "You cannot end a sentence with because because because is a conjunction"
print("Find for 'because' is: ", because_string.find('because'))
print("rFind for 'because' is: ", because_string.rfind('because'))

# Q25
print(because_string[:because_string.find('because')] + because_string[because_string.rfind('because'):])

# Q28
print('Coding For All starts with coding? ', company.startswith('Coding'))
print('Coding For All ends with coding? ', company.endswith('coding'))

# Q30
print("Spaces stripped from '   Coding For All      ': ", '   Coding For All      '.strip(' '))

# Q31
print("Does '30DaysOfPython' return true against isidentifier()?: ", '30DaysOfPython'.isidentifier())
print("Does 'thirty_days_of_python' return true against isidentifier()?: ", 'thirty_days_of_python'.isidentifier())

# Q32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("Combined list of libraries: ", '# '.join(libraries))

# Q33
print('I am enjoying this challenge.\nI just wonder what is next.')

# Q34
print("Name\tAge\tCountry\tCity\nMurtaza\t35\tFinland\tHelsinki")

# Q35
print('---')
print("radius = {}".format(10))
print("area = {} * {} ** {}".format(3.14, 'radius', 2))
print("The area of a circle with radius {} is {} meters square.".format(10, 314))

# Q36
a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
