# 6) შექმენი ცარიელი set, for ციკლით დაამატე მას ყველა კენტი რიცხვი 2-დან 8-მდე.

set1=set()
for i in range(2,9):
    if i % 2 !=0:
        set1.add(i)
print(set1)