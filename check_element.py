arr=[1,2,3,4]
flag=0
ele=4
for i in range(0,len(arr)):
    if(arr[i]==ele):
        print("Element found")
        flag=1
        break
if(flag==0):
    print("Element not found")


if 14 in arr:
    print("element exists in list")
else:
    print("Element not found")