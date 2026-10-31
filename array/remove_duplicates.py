

# arr = list(map(int, input("Enter array elements: ").split()))

arr=[0,1,1,2,2,3,4,5,6,6,6,7,8]
print(list(set(arr)))
n=len(arr)
c=0
s1=set()
for i in range(n):
    s1.add(arr[i])


print(s1)

print(len(arr)-len(s1))