# Creating a list
list_1 = ['banana', 'apple', 'orange']
list_2 = ['banana', '123', True, None, 3, '3']  # used
list_3 = list()
print(list_2)
# Retrieve list
print('--------------LEN LIST----------------')
print(len(list_2))
print('--------------INDEX OF----------------')
print(list_2.index(True))
print('--------------COUNT IN----------------')
print(list_2.count(3))
print('--------------LOOP IN-----------------')
for item in list_2:
    print(item)

print('----------LOOP IN WITH KEY-----------')
for index, item in enumerate(list_2, start=1):
    print(f'{index} - {item}')

print('--------------APPEND ITEM------------')
list_2.append(100)
print(list_2)
print('append multi-items')
list_2.extend([1, '1000'])
print(list_2)
print('--------------INSERT ITEM------------')
list_2.insert(1, 999)
print(list_2)
print('--------------REMOVE ITEM------------')
list_2.pop()
print('pop without argument: ', list_2)
list_2.pop(1)
print('pop with argument is a position: ', list_2)
list_2.remove(3)
print('remove value 3: ', list_2)
del list_2[0]
print('remove position 0: ', list_2)

print('--------------SORTING LIST------------')
my_list = [1, 8, 2, 3, 4, 6, 4, 6, 7]
# it's change in variable address
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print('reverse sorting: ', my_list)
# Return a new list
new_list = sorted(my_list)
print('new list: ', new_list)
new_list = sorted(my_list, reverse=True)
print('new list reverse: ', new_list)
new_list = list(reversed(my_list))
print('new list with use reversed(): ', new_list)

print('-----------USEFUL OPERATIONS----------')
# sum
print('sum in array 2: ', sum(my_list))
# max
print('max in array 2: ', max(my_list))
