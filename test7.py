fruits = ["pomme", "banane", "orange", "citron"]
fruit_recherche = "fraise"
trouve = False
for i in range(len(fruits)):
  if fruits[i] == fruit_recherche:
    trouve = True
    break
if trouve:
  print(fruit_recherche, "est dans le tableau")
else:
  print(fruit_recherche, "n'est pas dans le tableau")
