# 7) ფუნქცია აბრუნებს რიცხვების ჯამს 1–დან n–მდე.

def sum_of_n(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

n = int(input("Enter number:"))
print(sum_of_n(n))