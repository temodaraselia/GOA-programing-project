# 8) (hard) იგივე თაფლის გამოყენებით, ამოშალეთ ის რიცხვები რომლებიც მეორდება (hint: set() function)

my_tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5,0,0,0,0,0,0,0)

def set_tuple(item):
    item = set(item)
    return tuple(item)


print(set_tuple(my_tuple))