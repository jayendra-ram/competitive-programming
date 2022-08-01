# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def __init__(self):
        self.child_sums = []
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        self.dfs(root,0)
        print(self.child_sums)
        return targetSum in self.child_sums
    
    def dfs(self, root: Optional[TreeNode], sum: int):
        if root == None:
            pass
        elif root.left == None and root.right == None:
            self.child_sums.append(sum+root.val)
        else:
            self.dfs(root.left,sum+root.val)
            sef.dfs(root.right,sum+root.val)
