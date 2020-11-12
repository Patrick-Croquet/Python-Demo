a = int(input("a:"))
b = int(input("b:"))
drapeau = True
while drapeau:
    a, b = b, a%b
    if b == 0:
        drapeau = False
    print(b)