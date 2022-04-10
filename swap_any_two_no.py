arr=[23,65,19,90]
pos1,pos2=1,3
# arr[pos1],arr[pos2]=arr[pos2],arr[pos1]
# print(arr)
first_el=arr.pop(pos1)
# print(first_el)
lasst_el=arr.pop(pos2-1)
print(lasst_el)
print(arr)
arr.insert(pos1,lasst_el)
arr.insert(pos2,first_el)
print(arr)