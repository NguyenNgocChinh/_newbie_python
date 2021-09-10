my_string = 'Hello world'
print(my_string, type(my_string))
print('------------GET CHACRACTER IN STRING----------------')
# The first char in my string
print('the first character is: ', my_string[0])
# The last char in my string
print('the last character is: ', my_string[-1])
# Substring
# Start at index 1 and go to index 5 *(not include 5)
print('substring 1 - 5 is: ', my_string[1:5])
# Start at index 0 and go to index 5 *(not include 5)
print('substring 0 - 5 is: ', my_string[:5])
# Start at index 6 and go to last index
print('substring 6 - lenght is: ', my_string[6:])
# Reverse string
print('string after reverse is: ', my_string[::-1])
# Take every sencond character
print('take every sencond character is: ', my_string[::2])
print('--------------------CONCAT STRING--------------------')
print(my_string + " 123!")
print('-----------JOIN to string and SPLIT to array---------')
my_list = my_string.split(' ')
print('array after split is: ', my_list)
print('string after join is: ', ' *** '.join(my_list))
print('---------------------LOOP STRING---------------------')
for char in my_string:
    print(char)
print('-------------------CHECK CHARACTER-------------------')
if 'w' in my_string:
    print('Founded character W in string')
else:
    print('Not found character W in string')
print('-------------------OPTIMZE STRING--------------------')
print('string after remove whitespace from both ends',
      '               I am    not alone     '.strip())
print('string after remove I from both ends: ', 'I am not alone'.strip('I'))

print('-------------------REPLACE STRING--------------------')
print('string after replace me -> you: ', 'Help me'.replace('me', 'you'))
print('-------------------CHECK BEGIN WITH-------------------')
print('check begin with "Need": ', 'Need to make fire'.startswith('Need'))
print('-------------------CHECK END WITH---------------------')
print('check end with "fire": ', 'Need to make fire'.endswith('fire'))
print('--------------FIND INDEX STRING CONTAINT--------------')
# Throw error if not found
print('index of "w" in string: ', 'Hello world'.index('w'))
# Return -1 if not found
print('index of "xx" in string: ', 'Hello world'.find('xx'))
print('--------------COUNT CHARACTER IN STRING--------------')
print('hello world'.count('l'))

print('--------------------TRANSFER STRING--------------------')
print('string after uppercase: ', 'string will be uppercase'.upper())
print('string after lowercase: ', 'STRING WILL BE LOWERCASE'.lower())
print('string after upper first char of string: ', 'lorem is sump'.capitalize())
print('string after upper first char of word: ', 'lorem is sump'.title())

print('--------------INCLUDE VARIABLE IN STRING---------------')
name = 'Chinh Coder'
age = 22
pi = 3.14151617
# %
my_string = 'Hello, my name is %s and age = %d' % (name, age)
print('%', my_string)
# .format()
my_string = 'Hello, my name is {} and pi = {:.2f}'.format(name, pi)
print('.format', my_string)
# f String
my_string = f'Hello, my name is {name} and age = {age}, pi = {pi:.3f}'
print('.format', my_string)
