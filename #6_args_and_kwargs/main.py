
# *args là 1 parameter kiểu là List ([1,2,3])
# **kwargs là 1 parameter kiểu là dictionary ({'key':'value'})
def example(a, b, *list, **dictionary):
    print('-----------POSITIONAL ARGUMENTS--------------')
    print(a, b)
    print('------------ARGUMENTS ARGUMENTS--------------')
    # Loop arguments *args
    for item in list:
        print(item)
    print('--------------KEYWORD ARGUMENTS--------------')
    # Loop keyword **kwargs
    for key, value in dictionary.items():
        print(f'{key} - {value}')


def main():
    example(1, 2, "Item 1", "Item 2", key1="value1", key2="value2")


if __name__ == '__main__':
    main()
