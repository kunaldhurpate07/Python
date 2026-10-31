

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0

    ##Inserting node from tail
    def tail_insert(self,data):
        curr=self.head

        if self.head==None:
             self.head=Node(data)
        else:
            while curr.next!=None:
                curr=curr.next
            curr.next=Node(data)
            
        self.n+=1

    def display(self):
            curr=self.head
    
            res=''
            while curr!=None:
                res=res+str(curr.data) + '->'    ## Extra thing just to exclude last ->  
                curr=curr.next
            return res[:-2]
    
l=LinkedList()


l.tail_insert(1)
l.tail_insert(2)
l.tail_insert(3)
l.tail_insert(4)
print(l.display())