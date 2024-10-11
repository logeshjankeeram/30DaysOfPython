#Iterate 0 to 10 using for loop, do the same using while loop.

for i in list(range(11)):
    print(i)

x=0
while x < 11:
    print(x)
    x = x+1


#Iterate 10 to 0 using for loop, do the same using while loop.
x = list(range(10,-1,-1))

for i in x:
    print(i)

x=11
while x > 0:
    x=x-1
    print(x)


"""Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
#8 x 8


row = 0
while row < 8:
    column = 0  # Reset column to 0 for each row
    while column < 8:
        print("#", end="")  # Use end="" to print in the same line
        column = column + 1
    print()  # Move to the next line after each row is printed
    row = row + 1
