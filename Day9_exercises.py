'''Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
'''
Age= int(input("Please enter your age"))  #mistake= forgot to convert input to int as input only takes string
if Age > 17:
    print('You are old enough to drive.')
else:
     print(f'You have to wait {18-Age} years to start driving')

'''Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. '''

myage=int(input('Enter my age: '))
yourage=int(input('Enter your age: '))

if myage>yourage and myage-yourage==1 :
    print(f"i am {myage-yourage} year older than you")
elif myage>yourage and myage-yourage>1 :
    print(f"i am {myage-yourage} years older than you")         #this solution assumes no need for validation aka perfect world
elif myage<yourage and yourage-myage>1 :
    print(f"You are {yourage-myage} years older than me")
elif myage<yourage and yourage-myage==1 :
    print(f"You are {yourage-myage} year older than me")
else:
    print('we are same age')

'''Write a code which gives grade to students according to theirs scores:

80-100, A
70-70, B
60-69, C

'''
grade=float(input('Enter student grade'))

if grade<=100 and grade >=80:
    print('grade is equal to A')
elif grade<80 and grade >=70:
    print('grade is equal to B')
elif grade<70 and grade >=60:
    print('grade is equal to C')
else:
    print('failed')


'''The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

'''
fruits = ['banana', 'orange', 'mango', 'lemon']

newfruit=input('enter fruit name without surname')

if newfruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(newfruit)
    print(fruits)



'''Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:'''