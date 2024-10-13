def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_number():
    number1=2
    number2=3
    total=number1+number2
    return total

print(add_two_number())
      

#function with parameter

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


#two parameters

def generate_full_name(firstname,secondname):
    space=" "
    fullname= firstname +space+secondname
    return fullname
print(f"full name is: {generate_full_name('logesh','jankeeram')}")

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


#Passing Arguments with Key and Value- order does not matter

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter

#Function Returning a Value - Part 2
#If we do not return a value with a function, then our function is returning None by default.

def print_name(firstname):
    return firstname
print_name('Asabeneh') 
print(print_name('Asabeneh'))


def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name                                      # return stops further execution of the function in case of if or loop,
                                                            # similar to break 
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
print(print_full_name(firstname='Asabeneh', lastname='Yetayeh'))

# we can pass default values to parameter. If in case we do not pass on any arguments when calling the function
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def calculate_age (birth_year,current_year = 2021):  #in this case we have one required parameter and one default parameter
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))


#Arbitrary Number of Arguments -if we don't know number of arguments 
'''If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number
 of arguments by adding * before the parameter name.'''

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3,5, 5)) # you can input many parameters


def generate_groups(team="Team1", *args):
    print(f"Team: {team}")  # Printing team name
    for name in args:
        print(f'name is {name}')

# Call to use the default team
generate_groups('Brook', 'David', 'Eyob') 


#Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)                                 #use x as parameter for f
print(do_something(square_number, 3)) # 27