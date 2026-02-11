# 2) იგივე თაფლის გამოყენებით, გამოიტანეთ კენტი და ლუწი რიცხვები

tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5, 0)

def Odd_or_Even(tuple):
    odd = []
    even = []
    for i in tuple:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)

    return f"Odd Numbers---{odd}----------Even Numbers----{even}"

   
print(Odd_or_Even(tuple))