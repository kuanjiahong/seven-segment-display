n = input("Enter birthday in format YYYYMMDD: ")

x = [int(i) for i in n]

ans = sum(x)
while len(str(ans)) >= 2:
    x = [int(i) for i in str(ans)]
    ans = sum(x)
print(ans)