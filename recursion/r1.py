## Print name n times
n=int(input("Enter number:"))

def name(n):
    if n==0:
        return
    print("Kunal")
    name(n-1)

name(n)