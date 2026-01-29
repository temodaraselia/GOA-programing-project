# #number=int(input("enter number:"))

# if number % 2==0:
#     print("luwia")
# else:
#     print("kentia")



# age=int(input("enter your age:"))

# if age>=18:
#     print("srulwlovani xar")
# else:
#     print("arasrulwlovani xar")





# number_list=[1,2,3,4,5,6,7]
# print(number_list[0:6])




# for i in range(1,6):
#     print(number_list[0])
    

# number=int(input("enter your age"))
# number1=int(input("enter your favorite number:"))
# print(number+number1)



#მომხმარებელს შემოატანინე პაროლი თუ პაროლი ტოლია "python123" -დაბეჭდე წვდომა მიღებულია სხვა შემთხვევაში დაბეჭდე პაროლი არასწორია

# password=input("enter your password:")
# password1="python123"
# if password==password1:
#     print("წვდომა მიღებულია")
# else:
#     print("პაროლი არასწორია")


#მომხმარებელს შემოატანინე  ქულა თუ ქულა 90 - 100 "შესანიშნავი შედეგი"       80 - 89 "ძალიან კარგი"    70-79 "დამაკმაყოფილებელი"        70 "გადამეორება გჭირდება"


# score=int(input("enter your score:"))

# if score >= 90 and score <= 100:
#     print("შესანიშნავი შედეგი")
# elif score >= 80 and score<=89:
#     print("ძალიან კარგი")
# elif score >= 70 and score <= 79:
#     print("დამაკმაყოფილებელი")
# else:
#     print("გადამეორება გჭირდება")


#შემოიყვანე მომხმარებლის სახელი და პაროლი: თუ username == "temo" და password == "1234" დაბეჭდე "შესვლა წარმატებით" სხვა შემთხვევაში "მონაცემები არასწორია"

# name=input("enter your name:")
# password=input("enter your password:")

# if name=="temo" and password=="1234":
#     print("შესვლა წარმატებით")
# else:
#     print("მონაცემები არასწორია")



#მომხმარებელს კითხე ასაკი და აქვს თუ არ აბილეთი : თუ ასაკი <10 ან ბილეთი არის "კი" შესვლა უფასოა. სხვა შემთხვევაში "გთხოვთ გადაიხადო 5 ლარი"


# age=int(input("enter your age:"))
# bileti=input("gaqvs bileti?:")


# if age<10 or bileti=="ki":
#     print("შესცლა უფასოა")
# else:
#     print("გთხოვთ გადაიხადო 5 ლარი")


# number1=int(input("enter number1:"))
# number2=int(input("enter number2:"))
# number3=int(input("enter number3:"))


# if number1>number2 and number1>number3:
#     print(number1,"udidesi ricxvia")
# elif number2>number1 and number2>number3:
#     print(number2,"udidesi ricxvia")
# else:
#     print(number3,"udidesi ricxvia")


def calculator(x,y,op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    else:
        return x // y
    
x = int(input("enter number:"))
y = int(input("enter number:"))
op = input("enter operator:")
print(calculator(x,y,op))



