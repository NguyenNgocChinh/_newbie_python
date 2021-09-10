students = [
    {'name': 'chinh', 'age': 22},
    {'name': 'an', 'age': 21},
    {'name': 'vu', 'age': 18},
]

new_list = sorted(students, key=lambda item: item['name'], reverse=True)

print(new_list)
