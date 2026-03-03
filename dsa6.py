class Node:
    def __init__(self,info , next=None):
        self.data=info
        self.next=next

class Singlylinkedlist:
    def __init__(self, head=None):
        self.head=head

    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head != None):
            t1=self.head
            while (t1.next != None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    def insertAtBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp

    def insertInMid(self,value,x):
        temp=Node(value)
        t1=self.head
        while (t1.next!= None):
            if(t1.data ==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next    


    def printLL(self):
        t1=self.head
        while(t1.next!= None):
            print(t1.data)
            t1=t1.next
        print(t1.data)

    def deleteLL(self,value):
        t1=self.head
        prev=t1
        while (t1.next!=None):
            if(t1.data==value):
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next 
        if(t1.data==value):
            prev.next=None


obj= Singlylinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)                                        
obj.insertAtEnd(30)  
obj.insertAtBeg(15)
obj.insertInMid(40,20)  
obj.deleteLL(40)

obj.printLL()