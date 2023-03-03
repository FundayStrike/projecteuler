danceMoves = ["<", "+", "&", ">"]
danceChar = input()
index = danceMoves.index(danceChar)
print("".join(2*(danceMoves[index:]+danceMoves[:index])))
