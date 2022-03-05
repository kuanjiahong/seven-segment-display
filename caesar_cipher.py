n = input("Enter the text: ")
k = ""
text = ''
while True:
    k = int(input("Enter a shift value: "))
    if k > 0 and k < 26:
        break
    print("Please key in a value between 1..25")

for i in n:
    enc = ""
    if i.isalpha():
        pass
        if i.isupper():
            if ord(i) + k > ord('Z'):
                enc = ord('A') +  (k - (ord('Z') - ord(i)) - 1)
                text += chr(enc)
            else:
                enc = ord(i) + k
                text += chr(enc)
        elif i.islower():
            if ord(i) + k > ord('z'):
                enc = ord('a') + (k - (ord('z') - ord(i)) - 1)
                text += chr(enc)
            else:
                enc = ord(i) + k
                text += chr(enc)
    else:
        text += i

print(text)