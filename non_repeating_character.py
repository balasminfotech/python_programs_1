str1="welcome to w3resources"
vowels=''
for i in range(0,len(str1)):
    if str1[i] not in vowels:
        vowels += str(str1[i])
print(vowels)

r="w3resource .  com  "
print(r.replace(" ",''))