# 3) (hard) იგივე თაფლის გამოყენებით, გაიგეთ მეორდება თუ არა ელემენტები ორჯერ ან მეტჯერ (hint: set() function), უნდა დააბრუნოს true ან false
 
tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5, 0)

def count(tuple):
    set1 = set(tuple)
    return len(tuple) == len(set1)


print(count(tuple))