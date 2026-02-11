# 10) BONUS - ტვინის საჭყლეტი
# იგივე თაფლის გამოყენებით, შემდეგ შექმენით ახალი სია, თუ რიცხვი დადებითია, მასში შეინახეთ მაგ რიცხვის კვადრატი, თუ ის რიცხვი უარყოფითია, 
# მაშინ შეინახეთ მაგ რიცხვის კუბი, სხვა შემთხვევაში (თუ ნულია), უბრალოდ ჩაამატეთ. არანაირი ცვლილება ამ შემთხვევაში.

my_tuple = (1, 2, 3, -4, 50, -6, 89, -100, 700, -3, 0.5)

def new_list(item):
    result2 = []
    result3 = []
    positive_square = []
    negative_cube = []
    for i in item:
        if i >0:
            result2.append(i)
        else:
            result3.append(i)
    for i in result2:
        positive_square.append(i**2)
    for i in result3:
        negative_cube.append(i**3)
    return f"Positive Square = {positive_square} --- Negative Cube = {negative_cube}"



print(new_list(my_tuple))