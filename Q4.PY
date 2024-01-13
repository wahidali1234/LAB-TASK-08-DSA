def inOrderSuccessor(root, node):
    if node.right is not None:
        return minValueNode(node.right)
    succ = None
    while root is not None:
        if node.val < root.val:
            succ = root
            root = root.left
        elif node.val > root.val:
            root = root.right
        else:
            break
    return succ

def inOrderPredecessor(root, node):
    if node.left is not None:
        return maxValue(node.left)
    pred = None
    while root is not None:
        if node.val > root.val:
            pred = root
            root = root.right
        elif node.val < root.val:
            root = root.left
        else:
            break
    return pred