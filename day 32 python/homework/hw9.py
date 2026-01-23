# 15) while ციკლით სეტიდან ამოშალეთ ლუწი რიცხვები(discard - ის გამოყენებით).

nums = {1,2,3,4,5,6,7,8,9,10,100,200,1000}
n = list(nums)
i = 0

while i<len(n):
    if n[i] % 2 == 0:
        nums.discard(n[i])
    i+=1

print(nums)

