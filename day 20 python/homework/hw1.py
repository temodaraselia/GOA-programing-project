# 1) შექმენი ცარიელი სია numbers და მომხმარებელს 3-ჯერ შეეკითხე რიცხვი
#  (input()), თითო შეყვანილი მნიშვნელობა დაამატე append()-ით. ბოლოს დაბეჭდე სია.

numbers=[]

num1=int(input("Enter numbers:"))
num2=int(input("Enter numbers:"))
num3=int(input("Enter numbers:"))

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)

col1=input("enter your color:")
col2=input("enter your color:")
col3=input("enter your color:")



numbers.append(col1)
numbers.append(col2)
numbers.append(col3)

print(numbers)
