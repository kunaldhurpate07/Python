n=12345
rev=0
while n>0:
    t=n%10
    rev=rev*10+t
    n=n//10

print(rev)

#shortcut
n=12345001

print(int(str(n)[::-1]))