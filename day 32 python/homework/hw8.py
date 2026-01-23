# 14) while ციკლით დაამატეთ ცარიელ სეტში 1- დან 20 - მდე რიცხვებ(update - ის გამოყენებით).

nums = set()
result = []
x = 0
y = 20
while x != y:
    x+=1
    result.append(x)
nums.update(result)
print(nums) 