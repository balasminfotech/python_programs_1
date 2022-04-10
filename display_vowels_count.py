str="welcome to w3resources"
vowels="aeiou"
count=0
for i in str:
    if i in vowels:
        print(i)
        count+=1
print(count)