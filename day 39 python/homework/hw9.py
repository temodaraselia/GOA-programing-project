# 9) იგივე თაფლის გამოყენებით, შექმენით ორი ახალი თაფლი: ერთში შეინახავთ ისეთ რიცხვებს, რომლებიც დადებითია, მეორეში კი ისეთ რიცხვებს, რომლებიც უარყოფითია

my_tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5)

def diferent_tuples(item):
    positive = []
    negative = []
    for i in item:
        if i>0:
            positive.append(i)
        else:
            negative.append(i)
    positive = tuple(positive)
    negative = tuple(negative)
    return f"Positive tuple = {positive} ----- Negative tuple = {negative}"




print(diferent_tuples(my_tuple))