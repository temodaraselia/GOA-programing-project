# 10) ფუნქცია იღებს სტრინგს და აბრუნებს რამდენი 'a' ან 'A' არის მასში.

def count_A(s):
    result1 = s.count("a")
    result2 = s.count("A")
    return f" a არის {result1}-ჯერ და A არის {result2}-ჯერ"

print(count_A("abgda"))