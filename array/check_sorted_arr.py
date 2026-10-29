

arr =[1,2,3,4,5,6]
# arr=[5,6,7,4,6]
c=0
for i in range(1,len(arr)):
    if arr[i]>=arr[i-1]:
        pass
    else:
        c+=1

if c==0:
    print("sorted")
else:
    print("Not Sorted")




def fun(arr):
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            pass
        else:
            return False
    return True

print(fun(arr))