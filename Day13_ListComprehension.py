# lst = [i for i in input("enter ths")]
# print(type(lst)) # list
# print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

'''Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]'''

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# print([i for i in numbers if i >=0])

'''Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]'''

# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# print(list([k for row in list_of_lists for i in row for k in i]))

'''Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]'''

# print([0 for i in range(7)])
# print([1 for i in range(7)])
# print([2]+[2**i for i in range(7)])
# result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
# print(result)

'''countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]'''

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# print([z.upper() for i in countries for j in i for z in j for i in range(len(z)) if i >=0 z.insert(i,z[i][:3])])

'''Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']'''

# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# print([[k[a]+" "+k[a+1]for a in range(len(k)) if a%2==0] for i in names for k in i])
'''Write a lambda function which can solve a slope or y-intercept of linear functions.

'''
# m= lambda x1,y1,x2,y2:(y2-y1)/(x2-x1)
# print(m(5, 5, 3,4,))