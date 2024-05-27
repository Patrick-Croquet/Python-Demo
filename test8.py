nombres = [5, 2, 4, 1, 3]
# Algorithme de tri par sélection
for i in range(len(nombres)):
  min_indice = i
  for j in range(i + 1, len(nombres)):
    if nombres[j] < nombres[min_indice]:
      min_indice = j
  nombres[i], nombres[min_indice] = nombres[min_indice], nombres[i]
print("Le tableau trié est :", nombres)