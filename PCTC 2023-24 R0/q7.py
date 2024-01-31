required = int(input())
interactions = 0
total = 0
while interactions < required:
  interactions += 5
  total += interactions
print(total-(interactions-required))
