# 4) ფუნქცია იღებს რიცხვს და თუ ის ლუწია, გაორმაგებს, წინააღმდეგ შემთხვევაში 3–ით გაიმრავლებს.



def if_Even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num * 3
print(if_Even(5))