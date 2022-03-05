n = input("Enter the text: ")

half_length = len(n) // 2

def palindrome(n: str):
    a_list = []
    for i in n:
        if not i.isspace():
            a_list += i.lower()
    
    half_length = len(a_list) // 2
    for i in range(half_length):
        if a_list[i] != a_list[-1 - i]:
            return False
    
    return True

if palindrome(n):
    print("Palindrome")
else:
    print("Not palindrome")