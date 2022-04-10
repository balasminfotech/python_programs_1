# s="abcde"
s=input("Enter a string: ")
# print(s[:])
# print(s[0:5])
# print(s[0:5:1])
# print(s[::])
# print(s[::-1])
reverse_string=s[::-1]
if s==reverse_string:
    print("Palindrome")
else:
    print("Not a palindrome")