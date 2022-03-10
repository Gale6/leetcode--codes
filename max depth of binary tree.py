def maxDepth(root) -> int:
    if root == None:
        return 0
    else:
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        result = max(left, right) + 1
    return result
