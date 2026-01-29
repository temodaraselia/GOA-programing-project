# 6) ფუნქცია აბრუნებს სიაში დადებითი რიცხვების რაოდენობას.

def len_postive(nums):
    result = []
    for i in nums:
        if i >0:
            result.append(i)
    return len(result)

print(len_postive([1,2,3,4,5,   -1,-2,-3,-4,-5]))