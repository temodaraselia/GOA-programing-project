# 1) დაპრინტეთ დადებითი, უარყოფითი რიცხვების და ნულების რაოდენობა კონკრეტული თაფლის გამოყენებით

tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5, 0)

def positive_zero_negative(tuple):
    positive = 0
    negative = 0
    zero = 0
    for i in tuple:
        if i>0:
            positive += 1
        elif i<0:
            negative += 1
        else:
            zero += 1
    return f"Positive len = {positive},---Negative len = {negative},---Zero len ={zero}"


print(positive_zero_negative(tuple))
