import math
print("hello")

# Day 1 - 30DaysOfPython Challenge
#excercise1
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(5 % 2)             # modulus remainder(%)
print(5 // 2)            # Floor division operator(//)

#excercise2
# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


#excercise3
#Find an Euclidian distance between (2, 3) and (10, 8)

#step 1 formula of Euclidian distance: d={\sqrt {(p_{1}-q_{1})^{2}+(p_{2}-q_{2})^{2}}}.}
"""thinking process. 

should we count the coordinates as individual numbers? for example x1 = 2 and y1 = 3?

Or should we count them as set or list? for eg {2,3}

formula should be d=sqrt(((x1-x2)**2)+((y1-y2)**2))

the easiest solution right now since this is day 1. i will define variable as x1 and x2 then plot in the formula.
"""

x1=2
y1=3
x2=10
y2=8
d=math.sqrt(((x1-x2)**2)+((y1-y2)**2))

print(d)

#interestingly in need to import the math module and then use the math.sqrt() function. 
#i did the mistake of not importing it and using only the sqrt() function. corrected now