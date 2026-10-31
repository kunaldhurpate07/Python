n=12345
x=0
while(n>0):
    temp=n%10
    x=x+temp
    n=n//10
    
print(x)

## Using functions
n=12345
sum=0
for x in str(n):
    sum=sum+int(x)

print(sum)