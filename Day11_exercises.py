import math
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def sum(n1,n2):
    x= int(n1)+int(n2)  #need to convert to int 
    return x
print(sum(input('entern1'),input('entern2')))



#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

import math

def area(r):
    ar=math.pi*int(r)*int(r)
    return ar
print(area(input('enter radius')))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*x):
    y=0
    for i in x:
        if type(i) is not int and type(i) is not float:
            return "Only intergers or float should be input"
        else:
            y += i
    return y

print(add_all_nums(1,2,2,3,3,3,'three',3))


'''Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
Write a function which converts °C to °F, convert_celsius_to-fahrenheit.'''

def convert_celsius_to_fahrenheit(cel):        
    F = (cel*(9/5)) + 32                 # /: float div (5/2→2.5), //: int div (5//2→2), %: modulo (5%2→1)
    return F
print(convert_celsius_to_fahrenheit(5))


'''Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.'''

def check_season(month):
    if month == "September" or month == "October" or month == "November":
        return "Autumn"
    elif month == "December" or month == "January" or month == "February":
        return "Winter"
    elif month == "March" or month == "April" or month == "May":
        return "Spring"
    elif month == "June" or month == "July" or month == "August":
        return "Summer"

print(check_season(input("Enter month")))

#the above is my solution, below is chatgpt:

def check_season(month):
    # Define the seasons based on the month
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'
    

#Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,y1,x2,y2):
    grad= (int(y2)-int(y1))/(int(x2)-int(x1))
    return grad
print(calculate_slope(input('enter x1'),input('enter y1'),input('enter x2'),input('enter y2')))


#Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.


import cmath                                              #mistake- i use import math instead of cmath - cmath deals with complex
                                                        #in the future is dealing with -ve root, use cmath
def solve_quadratic_eqn(a,b,c):
    x1=(-b+cmath.sqrt((b**2)-4*a*c))/(2*a)
    x2=(-b-cmath.sqrt((b**2)-4*a*c))/(2*a)
    return x1,x2
print(solve_quadratic_eqn(4,2,1))


#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(x):
    for i in x:
        print(i)
       
  
    
print(print_list([1,2,3,4,5]))


#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).


def reverse_list(arr):
    reversed_array=[]
    for i in range(len(arr)-1,-1,-1):
        reversed_row=[]
        for j in range(len(arr[i])-1,-1,-1):
            reversed_row.append(arr[i][j])
        reversed_array.append(reversed_row)
    return reversed_array

original_2d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_2d_array = reverse_list(original_2d_array)
print(reversed_2d_array)
    
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    nlst=[]
    for i in lst:
        nlst.append(i.upper())
    return nlst

print(capitalize_list_items(['hello','idk']))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(lst,item):
  
    lst.append(item)
    return lst
print(add_item(['h','e',1,5],'rishab'))

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lst,item):
  
    lst.remove(item)
    return lst
print(remove_item(['h','e',1,5],'e'))

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(*x):
    y=0 
    for i in x:
        y += i
    return y
print(sum_of_numbers(1,2,3,3,4,5))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range

def sum_of_odds(*x):
    odd=0
    even=0
    for i in x:
        if (i%2) == 0:
            continue
        else:
            odd += i
    return odd
print(sum_of_odds(1,2,3,3,4,5))

#Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that range

def sum_of_odds(*x):
    odd=0
    even=0
    for i in x:
        if (i%2) == 0:
            odd += i
            
        else:
            continue
    return odd
print(sum_of_odds(1,2,3,3,4,5))

#Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.

def sum_of_odds(*x):
    odd=0
    even=0
    for i in x:
        if (i%2) == 0:
            even += 1
            
        else:
            odd += 1
    return odd,even
print(f'sum of odd and even respectively is :{sum_of_odds(1,2,3,3,4,5)}')

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(x):
    y=1
    for i in range(1,x+1):
        y= y*i
    return y
print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not

def empty(x):                  
    y=0
    for i in x:
        if i!='':
            y+=1
    if y>0:
        return "not empty"
    else:
        return "empty"

print(empty(()))

#my answer above vs chatgpt down

def is_empty(param):
    if isinstance(param, (str, list, tuple, dict)):
        return len(param) == 0  # Return True if the length is 0
    return False  # For non-empty values or unsupported types, return False

#or

def is_empty(param):
    return not param  # Returns True if param is empty or evaluates to False

print(is_empty([]))


#Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation).

lst = [2,3,4,5,5,6,7,8]

def calculate_mean(x):
    sum=0
    for i in x:
        sum+=i

    return sum/len(x)
print(calculate_mean(lst))


lst = [int(i) for i in input("enter numbers separated by spaces: ").split()]  #need to remember this by heart
lst.sort()
def calculate_median(x):
    median=0
    n=len(x)
    if n%2==0:
        median=((x[n//2])+(x[(n//2)-1]))/2       #index can only be integer so need to use integer division
    else:
        median=x[n//2]
    return median
print(calculate_median(lst))


lst = [int(i) for i in input("Enter numbers separated by spaces: ").split()]
frequency = {}

def calculate_mode(x):
  
    for num in x:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1  
    
    max_count = 0  
    mode = []  
    
    
    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            mode = [num]  
        elif count == max_count:
            mode.append(num)  
    
    return mode


print("Mode(s):", calculate_mode(lst))


