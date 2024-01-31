valid = 0
for i in range(12):
  num = input()
  valid += int(int(num[-1]) == int(num[0])+1 or int(num[-1]) == int(num[0])-1)
print(valid)
