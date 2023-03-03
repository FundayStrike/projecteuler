chars = input()
print("I" if chars.count("I") < 2 else "M" if chars.count("M") < 1 else "C" if chars.count("C") < 3 else "W")
