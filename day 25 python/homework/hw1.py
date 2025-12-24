# 1) შექმენით ფუნქცია, მიიღებთ რიცხვს, თუ კენტია დააბრუნეთ "კენტია", თუ ლუწი - "ლუწია"

def Even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number=int(input("enter number:"))
print(Even_odd(number))

