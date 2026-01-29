# 3) ფუნქცია იღებს სიას რიცხვებისგან და აბრუნებს მხოლოდ დადებითების ჯამს.

def sum_of_positive(nums):
    result = []
    for i in nums:
        if i>0:
            result.append(i)
    return sum(result)

print(sum_of_positive([1,2,3,4,5,   -1,-2,-3,-4,-5]))