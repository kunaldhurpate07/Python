n=234
n1=n
a=0
while n>0:
    t=n%10
    a=a+t*t*t
    n=n//10

if n1==a:
    print("Number is armstrong")
else:
    print("not Armstrong")

