# 7) იგივე თაფლის გამოყენებით, შეაბრუნეთ მთლიანი თაფლი

my_tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5)

def reversed_tuple(item):
    return item[10:0:-1]



print(reversed_tuple(my_tuple))