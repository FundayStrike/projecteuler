pass1 = input()
pass2 = input()
pass3 = input()
if pass1 == pass2 and pass2 == pass3:
  print("OK")
elif pass2 != pass1 and pass3 != pass1:
  print("BOTH MISMATCH")
elif pass2 != pass1:
  print("ENTRY 2 MISMATCH")
else:
  print("ENTRY 3 MISMATCH")
