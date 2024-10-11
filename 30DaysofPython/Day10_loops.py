'''We had some issues - i couldn't commit because i changed my username on github but we are right back and
will complete 1/3 of the course today.
'''

#while loop

count = 0
while count < 5:
    print(count)
    count = count + 1


#break in while loop

count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break

#continue in while loop

count = 0
while count < 5:
    if count == 3:
        count = count + 1
    continue
    print(count)
    count = count + 1


#for loop in list

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: 
    print(number)       


#for loop in string

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

print(f"{range(11)}")