# 5) ფუნქცია იღებს სტრინგს და აქრობს ბოლო სიმბოლოს, თუ ის "!" არის.

def symbols(s):
    s = list(s)
    if s[-1] == "!":
        s.remove("!")
        s = "".join(s)
        return s
    else:
        s = "".join(s)
        return s
    

print(symbols("hello!"))