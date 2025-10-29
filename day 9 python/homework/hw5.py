#5) დაწერეთ კოდი, სადაც პროდუქტები რისიც ყიდვა გვინდა, ჯამში ღირს 22.50 ლარი, თუ გვაქვს ამაზე მეტი,
#  მაშინ გამოვიტანოთ 'ხურდა: 22.50 - ფული რაც გვაქვს', თუ არ გვყოფნის მაშინ გამოვიტანოთ: 'გაკლია 22.50 - რაც გვაქვს'

money=float(input("how much do you have:"))
product=float("22.50")
if money>product:
    print(money-product, " ლარი", "ხურდა")
elif money==product: 
    print("ფული გვყოფნის")
else:
    print(money-product," ლარი","გაკლია")































































































