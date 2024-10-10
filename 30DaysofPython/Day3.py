import math
# Exercise 1

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions as it gives errors
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

#Exercise 2

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)


#Exercise 3

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('L in Logesh', 'L' in 'Logesh') # True - A found in the string
print('B in Logesh', 'B' in 'Logesh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True


'''Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
Calculate the perimeter of the triangle (perimeter = a + b + c).'''

a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))

print('Perimeter is: ',a+b+c)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#x^2 + 6x + 9=0
#
a=float(input("Enter value a: "))
b=float(input("Enter value b: "))
c=float(input("Enter valeue c: "))

x=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
print('x= ',x)
x=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
print('x= ',x)