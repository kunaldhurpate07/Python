

arr=[5,1,2,3,4,5,6]

max1=arr[0]
max2=-1
for i in range(1,len(arr)):
    if max1<arr[i]:
        max2=max1
        max1=arr[i]
    elif arr[i]< max1 and arr[i]>max2:
        max2=arr[i]