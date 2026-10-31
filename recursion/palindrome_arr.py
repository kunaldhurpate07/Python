

arr = list(map(int,input("Enter array elements: ").split()))

print(arr)

def fun(arr,s,e):
    if arr[s]>=arr[e]:
        return True
    if arr[s]!=arr[e]:
        return False
    return fun(arr,s+1,e-1)

if fun(arr,0,len(arr)-1):
    print("The array is palindrome")
else:
    print("The array is not palindrome")