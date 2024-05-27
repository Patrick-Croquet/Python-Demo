def Trouve(a, b):
    i = 0
    while i < len(a) - len(b) and b != a[i:i+len(b)]:
        i += 1
    if b != a[i:i+len(b)]:
        return 0
    else:
        return i
    
Trouve("Patou", "aeiouy") 