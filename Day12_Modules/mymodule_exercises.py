'''# Writ a function which generates a six digit/character random_user_id.'''

# import random
# import string

# def random_user_id():
#     x=""
#     x=''.join(random.choices((string.ascii_letters + string.digits), k=6))
#     print(x)


#     return x

'''# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs 
# using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to 
# be generated.'''

# import random
# import string

# def user_id_gen_by_user():
#     a=int(input("Enter the number of characters"))
#     b=int(input("Enter the number of IDs"))
    
#     x=""
#     y=[]
#     for i in range(0,b):

#         x=''.join(random.choices((string.ascii_letters + string.digits), k=a))
#         y.append(x)
#         print(x)


#     return y


# import random
# import string

# def random_user_id():
#     x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#     print(x)
#     return x

# def user_id_gen_by_user():
#     a = int(input("Enter the number of characters: "))
#     b = int(input("Enter the number of IDs: "))
    
#     y = []
#     for _ in range(b):
#         x = ''.join(random.choices(string.ascii_letters + string.digits, k=a))
#         y.append(x)
#         print(x)

#     return y

# # Call the functions to test
# print("Generating a single random user ID:")
# random_user_id()  # Call the first function to generate a 6-character user ID

# print("\nGenerating multiple user IDs based on user input:")
# user_id_gen_by_user()  # Call the second function to generate multiple IDs


'''# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)'''


# import random

# def rgb_color_gen():
#     # Generate three random integers for RGB components
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
    
#     # Return the RGB color as a string
#     return f"rgb({r}, {g}, {b})"

# # Print the generated RGB color
# print(rgb_color_gen())

'''# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 
# and first 6 letters of the alphabet, a-f. Check the task 6 for output'''

import random
import string

def list_of_hexa_colors():
    x=''
    b = int(input("Enter the number of hex: "))
    c=[]
    
    h="abcdef1234567890"


    for _ in range(0,b):
        x = "".join(random.choices(h, k=6))
        c.append(f"#{x}")
    
    # Return the RGB color as a string
    return c

# Print the generated RGB color
print(list_of_hexa_colors())

'''Write a function list_of_rgb_colors which returns any number of RGB colors in an array.'''

import random
import string

def list_rgb_colors():
    x=int(input("enter number of colours"))
    y=[]
   

    for _ in range(0,x):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        y.append(f"{r},{g},{b}")
    
    return y
print(list_rgb_colors())

'''Write a function generate_colors which can generate any number of hexa or rgb colors.'''

def generate_colors():
   
    return f"{list_of_hexa_colors()}{list_rgb_colors()}"



