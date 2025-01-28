str1 = input("Enter a string: ")
result = ""
i = 0
while i < len(str1):
    char = str1[i]
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
    i += 1
print("Lower case string:", result)
