word = input()
ans = ['' for i in range(6)]
for i in range(len(word)):
  ans[i] = word[(i+2)%6]
print(''.join(ans))
