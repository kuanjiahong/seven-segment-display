def anagram(x:str, y:str):
    if x == "":
        return False
    if y == "":
        return False
    x = x.replace(" ", "")
    y = y.replace(" ", "")
    x = list(x.lower())
    y = list(y.lower())

    for i in x:
        if i not in y:
            return False
    
    return True

x = input()
y = input()

if anagram(x, y):
    print("Anagrams")
else:
    print("Not anagrams")
