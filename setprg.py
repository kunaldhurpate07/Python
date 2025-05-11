empSet = set()
st=type(empSet)
print(st)

nempSet = {1,3,4,'abc'}
st1=type(nempSet)
print(st1)
print(nempSet)

#mutability of set
nempSet = nempSet | {1,2,3}
print(nempSet)