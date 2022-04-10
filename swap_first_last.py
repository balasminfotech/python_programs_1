arr=[1,2,3,4,5]
# arr[0],arr[-1]=arr[-1],arr[0]
print(arr)
l=len(arr)
# print(l)
temp=arr[0]
arr[0]=arr[l-1]
print(arr[0])
arr[l-1]=temp
# print(arr)