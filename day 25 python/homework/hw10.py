# 10) შექმენით ფუნქცია, მიიღებთ სტრინგს. თქვენი დავალებაა მაგ სტრინგს მოაშოროთ ყველანაირი ცარიელი ადგილი და დატოვოთ მხოლოდ რიცხვები,
# სიმბოლოები და ასოები
#"    gaaa marjoba     " -> "gaamarjoba"
#"ki ara         vashli" -> "kiaravashli"
#codewars-ების მსგავსი


def string(s):
    a="".join(s)
    return a

s=input("enter:")
print(string(s))

