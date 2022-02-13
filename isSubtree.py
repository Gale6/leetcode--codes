# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                
        
        def sameTree(TreeOne,subRoot):
            if not TreeOne and not subRoot:
                return True
            if TreeOne and subRoot and TreeOne.val == subRoot.val:
                return (sameTree(TreeOne.left,subRoot.left) and
                        sameTree(TreeOne.right,subRoot.right)                    
                )
            return False
        
        
        if subRoot == None:
            return True
        if root == None:
            return False
        
        if sameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or
               self.isSubtree(root.right,subRoot))


                    



