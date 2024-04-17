# Murtaza
# 4/16/2024

# Imports
import math

# Q1 - 3
age = 24
height = 172.72
complex_num = 4 + 1j

# Q4
base = int(input("Enter Base of Triangle: "))
height = int(input("Enter Height of Triangle: "))
print("The area of the triangle is: ", base*height*0.5)

# Q5
side_a = int(input("Enter length of side A: "))
side_b = int(input("Enter length of side B: "))
side_c = int(input("Enter length of side C: "))
print("The perimeter of triangle is: ", side_a + side_b + side_c)

# Q6
width = int(input("Enter width of rectangle: "))
length = int(input("Enter length of rectangle: "))
print("Area of rectangle is {}m^2 and Perimeter is {}m".format(width*length, 2*(width + length)))

# Q7
radius = int(input("Enter radius of the circle: "))
print("Area of circle is {} and Circumfrence is {}".format(math.pi*pow(radius, 2), 2*math.pi*radius))

# Q8 - 10
y = lambda x: (2*x) - 2
print("Slope of equation is: ", (y(10) - y(4))/(10 - 4)) # (y(10), 10) & (y(4), 4)
print("Euclidean Distance between points is: ", math.dist([2,2], [6,10]))
print("Difference in slopes: ", (y(10) - y(4))/(10 - 4) - math.dist([2,2], [6,10]))

# Q11
y = lambda x: x**2 + 6*x + 9
x_val = -100
flag = False
while not flag:
    if y(x_val):
        x_val += 1
    else:
        flag = True
        print("X Value that returns a value of 0 for Y is: ", x_val)
        break

# Q12
print("Is length of 'python' greater than 'dragon'?: ", len('python') > len('dragon'))
flag = True if 'on' in 'python' and 'on' in 'dragon' else False
print("Is 'on' in both 'python' AND 'dragon'? ", flag)

# Q14
statement = "I hope this course is not full of jargon."
if 'jargon' in statement: print("'jargon' found in sentence")

# Q15
print("'on' in python/dragon", 'on' not in 'python' and 'on' not in 'dragon')

# Q16
print(str(float(len('python'))))

# Q17
is_even = lambda x: True if x % 2 == 0 else False
print("Is 13 even?: ", is_even(13))
print("Is 12 even?: ", is_even(12))

# Q18
print(True if 7 // 3 == int(2.7) else False)

# Q19
print(type('10') == type(10))

# Q20
print("9.8 == 10?: ", int(9.8)==10)

# Q21
hours = int(input("Enter Hours(h): "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is: $", hours * rate)

# Q22
years = int(input("Enter number of years you have lived: "))
print("You have lived for {} seconds".format(years*365*24*60*60))

# Q23
print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125\n')
