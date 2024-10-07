#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a = 'Thirty'
b = 'Days'
c= 'Of'
d = 'Python'

string= a + " " + b+ " "+ c+ " "+d
print(string)

#Declare a variable named company and assign it to an initial value "Coding For All".
Company= "Coding For All"

#Print the variable company using print().
print(Company)

#Print the variable company using print().
print(len(Company))

#Change all the characters to uppercase letters using upper() method.
print(Company.upper())

#Change all the characters to lowercase letters using lower() method.
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

"""Won't do, very easy"""

#Cut(slice) out the first word of Coding For All string.
print(Company[0:6])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.

word = "Coding"

if word in Company:
    print('The string contains the word '+ word +'.') #as you can see, there is two way you can embed expressions in a string. 
                                                        #the first one is the traditional one, the second is the latest one.
else:
    print(f'The string does not contain the word "{word}".')


'''second way of doing it:'''

string = "Coding For All"
word = "Coding"

index = string.find(word)
if index != -1:
    print(f'The string contains the word "{word}" at index {index}.')
else:
    print(f'The string does not contain the word "{word}".')


#Replace the word coding in the string 'Coding For All' to Python.
string = "Coding For All"
word = "Coding"
print(f'the new string is: {string.replace("Coding","Python")}')

#Split the string 'Coding For All' using space as the separator (split())
string = "Coding For All"
print(string.split(" "))

#What is the character at index 0 in the string Coding For All.
string = "Coding For All"
print(f'the first character is: {string[0]}')

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym=[]
string = "Coding For All"
x= string.split()#to split by space

for word in x:  #for loop, run through each element in the list and assigns it to word
    acronym.append(word[0])  #appends word[0] to acronym each time
acronym1 = ''.join(acronym)  # joins [x, y, z] to xyz

print(acronym1)

#Use index to determine the position of the first occurrence of C in Coding For All.
string = "Coding For All"

print(string.index('For'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.

string = "Coding For All"

print(string.rfind('i'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string ='You cannot end a sentence with because because because is a conjunction'
print(string.index('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'

