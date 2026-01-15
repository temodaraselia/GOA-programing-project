# 8) შექმენი ორი ცარიელი set, პირველს დაამატე რიცხვები 1 და 2, მეორეს დაამატე რიცხვები 2 და 3, შემდეგ გააერთიანე ისინი.

set1 = set()
set2 = set()

set1.add(1)
set1.add(2)

set2.add(2)
set2.add(3)

result = set1.union(set2)
print(result)