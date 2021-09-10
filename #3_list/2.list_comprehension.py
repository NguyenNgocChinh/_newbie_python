'''
Giúp viết code ngắn hơn
'''

# new_list[<action> for <item> in <iteractor> if <some condition>]

words = 'hello word'

# for char in words:
#     print(char)

[print(char) for char in words]  # print single char
print([char for char in words])  # print array char

# print i % 2 == 0
print([i for i in range(0, 100) if i % 2 == 0])

############ EX ##################
transactions = [100, 200, 300, 400]
TAX_RATE = .08
SERVICE_CHARGE = .07


def get_price_tax_fee(bill):
    return bill * (1 + TAX_RATE + SERVICE_CHARGE)


print([get_price_tax_fee(bill) for bill in transactions])
