import string
import random
symbols = []
symbols = list(string.ascii_letters)
card1 = [0]*5
card2 = [0]*5
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
samesymbol = random.choice(symbols)
symbols.remove(samesymbol)
if pos1 == pos2 :
    card1[pos1] = samesymbol
    card2[pos1] = samesymbol
else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
for i in range(0,5):
    if i!= pos1 and i != pos2 :
        alpha1 = random.choice(symbols)
        symbols.remove(alpha1)
        alpha2 = random.choice(symbols)
        symbols.remove(alpha2)
        card1[i] = alpha1
        card2[i] = alpha2
        i = i+1
print(card1)
print(card2)
print("input the common character :")
inputt = input()
if inputt == samesymbol:
    print("HURRAYYY 7 CROOREEEEE")
else:
    print("BRO U CAN'T BE REAL, LOSING THIS EASY GAME")