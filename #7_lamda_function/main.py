# <variable> = lamda <parameter>: return <action>
from functools import reduce
lambda so: so + 69
lambda x, y, z: x + y - z

numbers = [1, 9, 2, -1, 3, -3, 5]
coor = [(5, 6), (-1, 5), (4, 2), (2, 1)]
text = ['hello', 'cac ban', 'hehe']
students = [
    {'name': 'chinh', 'age': 22},
    {'name': 'an', 'age': 18},
    {'name': 'tam', 'age': 19},
]
'''
SORT
'''
# Default sort item[0]
print('Default sorted: ', sorted(coor))

# Sort with item[1]
print('Sort with [1]: ', sorted(coor, key=lambda item: item[1]))

print('Sort abs: ', sorted(numbers, key=lambda item: abs(item)))


'''
MAP
'''
print(list(map(lambda item: item.title(), text)))
print([x.title() for x in text])  # Same

print(list(filter(lambda item: item % 2 != 0, numbers)))
print([x for x in numbers if x % 2 != 0])  # Same

'''
REDUCE
'''
print(reduce(lambda a, b: a if a > b else b, numbers))
