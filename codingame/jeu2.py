import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def find_closest_powers(powers):
  """
  CHEVAUX DE COURSE
  Trouve les deux puissances les plus proches dans un ensemble de puissances.

  Args:
    powers: Un ensemble de puissances.

  Returns:
    Une liste contenant les deux puissances les plus proches.
  """

  powers.sort()
  closest_powers = []
  closest_distance = float("inf")
  for i in range(len(powers) - 1):
    distance = abs(powers[i] - powers[i + 1])
    if distance < closest_distance:
      closest_distance = distance
      closest_powers = [powers[i], powers[i + 1]]
  return closest_powers

def main():
  """
  Programme principal.
  """

  n = int(input())
  powers = []
  for _ in range(n):
    powers.append(int(input()))
  closest_powers = find_closest_powers(powers)
  print(closest_powers[1] - closest_powers[0])

if __name__ == "__main__":
  main()
