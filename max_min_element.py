arr=[1,2,3,4,5]
max=min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print("Max is", max)

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print("Min is", min)