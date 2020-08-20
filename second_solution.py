class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None

def insert(node,data):
    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)

    return node

def height_of_tree(node): 
    if node is None: 
        return 0
    else:  
        lDepth = height_of_tree(node.left) 
        rDepth = height_of_tree(node.right) 
 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1

root = insert(None,30)
root = insert(root,40)
root = insert(root,50)
root = insert(root,10)
root = insert(root,5)
root = insert(root,15)
root = insert(root,20)
root = insert(root,25)
print(height_of_tree(root))