# 6) იგივე თაფლის გამოყენებით, გადაამრავლეთ ყველა რიცხვი ერთმანეთზე

my_tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5)

def Reproduction(item):
    result = 0
    index = 0
    index2 = 1
    while index2 !=len(item):
        result +=  item[index] * item[index2]
        index += 1
        index2 += 1
    return result

print(Reproduction(my_tuple))