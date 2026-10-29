n=int(input("Enter the number:"))
n2=n
rev=0
while n>0:
    t=n%10
    rev=rev*10+t
    n=n//10

if rev==n2:
    print("palindrome")
else:
    print("Not Palindromr")