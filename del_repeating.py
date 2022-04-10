arr=["geeks","for","geeks"]
n=2
count=0
word="geeks"
for i in range(0,len(arr)):
    if(arr[i]==word):
        count=count+1
    if count==n:
        del arr[i]
print(arr)