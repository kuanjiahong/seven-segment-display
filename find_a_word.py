tofind = input()
the_text = input()
result = ""
for i in tofind:
    if the_text.find(i) == -1:
        result = False
        break
    result = True

if result:
    print("Yes")
else:
    print("No")