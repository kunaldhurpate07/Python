
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,):
        self.head=None
        self.n=0

    #Insert at Head
    def head_insert(self,data):
        n = Node(data)


        n.next=self.head
        self.head=n
        self.n+=1

    ## Insert from Tail
    def tail_insert(self,data):
        curr=self.head
        if self.head==None:
            self.head=Node(data)
            return
            

        while curr.next!=None:
            curr=curr.next

        curr.next=Node(data)
        self.n+=1

    ## Insert at Middle
    def mid_insert(self,after,data):
        curr=self.head
        new = Node(data)

        if self.head==None:
            return "Empty Linked List"

        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next

        if curr!=None:
                new.next=curr.next
                curr.next=new
                return
        else:
            return "Not found"
    
    #Print Elements from Head
    def travers(self):
        curr=self.head
        res = ''
        

        while curr!=None:
            res=res + str(curr.data) +'->'
            curr=curr.next
        return res[:-2]

    def clear(self):
        self.head=None
        self.n=0


    ## Delete from head
    def head_del(self):
        if self.head==None:
            print("Empty")
        self.head=self.head.next
        self.n-=1

    #Delete from tail
    def tail_dele(self):
            if self.head==None:
                print("Empty List")
                return
    
            if self.head.next==None:
                return ll.head_del()
    
            while curr.next.next!=None:
                curr=curr.next
    
            curr.next=None
            self.n-=1

    



ll=LinkedList()
# ll.head_insert(1)
# ll.head_insert(2)
# ll.head_insert(3)

# print(ll.travers())


# ll.tail_insert(4)
ll.tail_insert(5)

print(ll.travers())

ll.mid_insert(4,6)
print(ll.travers())

ll.head_del()
print(ll.travers())

ll.tail_dele()
