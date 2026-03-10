class Node:
    def __init__(self,value):
        self.left= None
        self.right= None
        self.data= value
    def insert(root,value):
        if(root==None):
            return node(value)
        if(root.data==value):
            return root
        if(root.data>value):
            root.left=insert(root.left,value)
        else:
            root.right=insert(root.right,value)
        return root
def Inorder(root):
    if(root!=None):
        Inorder(root.left)
        print(root.data,end=" ")
        Inorder(root.right)
root=Node(20)
root.left=Node(15)
root.right=Node(30)
root.left.left=Node(12)
root.left.right=Node(18)
Inorder(root)                                    