arr=[1,2,3,4,3,4]
count=0
ele=3
for i in range(0,len(arr)):
    if(arr[i]==ele):
        count=count+1
print("{} has appeared {} times".format(ele,count))

x=arr.count(ele)
print(x)