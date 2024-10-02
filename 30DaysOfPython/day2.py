import math
#Python Variable Name Rules

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

'''Excercise 1'''

first_name = 'Logesh' #need to be between ''
last_name = 'Jankeeram'
country = 'Mauritius'
city = 'Montida'
age = 23
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python'] #this is a list
person_info = {
   'firstname':'Logesh',
   'lastname':'Jankeeram',
   'country':'Mauritius',
   'city':'montida'
   } #this is a dictionary

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


#exercise 2 - input

first_name=input('what is your first name?')
print(first_name)

#exercise 3- Casting: Converting one data type to another data type.

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int',int(float(num_str)))     # '''this would not work as int has a base of 10 meaning we would need to first convert to float then to int'''
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Logesh'
print(first_name)               # 'Logesh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['L', 'o', 'g', 'e', 's', 'h']


'''The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords'''

radius=float(input("enter radius")) # this returns a string by default so need to convert to float
area_of_circle= math.pi* (radius**2) #cannot use pi directly need to use math.pi
print(area_of_circle)

#test
