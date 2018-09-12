def check_subtrees(T1, T2):
    t1_arr = []
    t2_arr = []
    
    helper(T1, t1_arr)
    helper(T2, t2_arr)
    
    print (t1_arr, t2_arr)

    t1_str = "".join(str(x) for x in t1_arr)
    t2_str = "".join(str(y) for y in t2_arr)

    print (t1_str, t2_str)

    return t1_str[t1_str.index(t2_str)] != None

def helper(T, str_rep):
    if not T:
        str_rep.append("N")
        return
        
    str_rep.append(T.val)
    helper(T.left, str_rep)
    helper(T.right, str_rep)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root2 = Node(1)
root2.left = Node(4)
root2.right = Node(5)

print (check_subtrees(root,root2))
