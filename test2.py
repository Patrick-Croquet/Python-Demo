a = int(input("a:"))
b = int(input("b:"))
while b != 0:
    a, b = b, a%b
    print('a:',a, 'et b:', b)
print(a)

print("--------")
i = 0
while i < 10:
    i += 1 # Pour ne pas avoir une boucle infinie
    if i%2 == 0: # Si i est pair
        continue
    print(i)