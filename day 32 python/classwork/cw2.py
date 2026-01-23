# 2) შექმენით ცარიელი სეტი, დაამატეთ მასში რამდენიმე რიცხვი და შემდეგ ამოიტანეთ ის რიცხვები რომლებიც კენტია.

my_set = set()
my_set.update([1,2,3,4,5,6,7,8,9,10])
my_set = list(my_set)

for i in my_set:
    if i % 2 != 0:
        my_set.remove(i)
print(set(my_set))