#Objective: Find the first non-repeated character in a string


str = input("Enter a string")

alphabet = [25]
print(alphabet)

flag = 0
i = 0
while i < len(str):
    pos = ord(str[i])-97
    print(pos)
    alphabet[pos] += 1
    i += 1
    print(i)

for i in alphabet:
    if alphabet[i] == 1:
        print(str(i+97))
        break