import math

# A ← Sin(B) Aucun problème
B = 0.5
A = math.sin(B)
print("Aucun problème:", A)

# A ← Sin(A + B * C) Aucun problème
C = 0.3
A = math.sin(A + B * C)
print("Aucun problème:", A)

# B ← Sin(A) – Sin(D) Erreur ! D est en caractère
D = "0.7"
# Correction: convertir D en radians
B = math.sin(A) - math.sin(D)
print("Erreur ! D est en radians:", B)

# D ← Sin(A / B) Aucun problème… si B est différent de zéro
if B != 0:
    D = math.sin(A / B)
    print("Aucun problème:", D)
else:
    print("Erreur ! B est égal à zéro")

# C ← Cos(Sin(A) Erreur ! Il manque une parenthèse fermante
C = math.cos(math.sin(A))  # Correction: ajouter une parenthèse fermante
print("Aucun problème:", C)
