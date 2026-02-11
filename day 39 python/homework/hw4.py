# 4) იგივე თაფლის გამოყენებით გამოიტანეთ უდიდესი და უმცირესი რიცხვი (max() / min() ფუნქციების გარეშე)

my_tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5, 0)

def max_or_min(item):
    max1 = item[0]
    min1 = item[0]
    for i in item:
        if i>max1:
            max1 = i
        elif min1 >i:
            min1 = i
    return f"Max = {max1}---Min = {min1}"

print(max_or_min(my_tuple))