# 12) for ციკლით დაამატეთ ცარიელ სეტში 1 - დან 20 - მდე რიცხვები(update - ის გამოყენებით).

set1 = set()
result =[]
for i in range(1,20+1):
    result.append(i)

set1.update(result)
print(set1)