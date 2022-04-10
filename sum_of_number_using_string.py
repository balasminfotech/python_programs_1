x="123abcd45"
res=0
st=''
for i in x:
    if i.isdigit():
        y=int(i)
        res =res+y
    elif i.isalpha():
        y=str(i)
        st =st+y
print(st)
print(res)