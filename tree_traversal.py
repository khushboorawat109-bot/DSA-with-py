class Node:
    def __init__(self,value):
        self.left= None
        self.right= None
        self.data= value
def preorder(root):
    if(root != None):
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def Inorder(root):
    if(root != None):
        Inorder(root.left)
        print(root.data,end=" ")
        Inorder(root.right) 
def Postorder(root):
    if(root != None):
        Postorder(root.left)
        Postorder(root.right)
        print(root.data,end=" ")

root=Node(1)
root.left=Node(3)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(8)
preorder(root) 
Inorder(root)
Postorder(root)

