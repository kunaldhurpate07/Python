

class Node:
    def __init__(self,data):
        self.data=data
        self.next =None
        

class LinkedList:
    def __init__(self):
        self.head=None

    ##Inserting node to head
    def insert_head(self,data):
        n1=Node(data)
        n1.next=self.head
        self.head=n1

    ## Display linked list
    def display(self):
        curr=self.head

        res=''
        while curr!=None:
            res=res+str(curr.data) + '->'    ## Extra thing just to exclude last ->  
            curr=curr.next
        return res[:-2]

l=LinkedList()

l.insert_head(3)
l.insert_head(4)
print(l.display())