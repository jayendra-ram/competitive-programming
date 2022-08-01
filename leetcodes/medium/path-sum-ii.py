# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def __init__(self):
        self.child_sums = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return []
        self.dfs(root,0,[])
        output = []
        for sum, path in self.child_sums:
            if sum == targetSum:
                output.append(path)
        return output
    
    def dfs(self, root: Optional[TreeNode], sum: int, path):
        if root == None:
            pass
        elif root.left == None and root.right == None
            self.child_sums.append((sum+root.val,path+[root.val]))
        else:
            self.dfs(root.left,sum+root.val,path+[root.val])
            self.dfs(root.right,sum+root.val,path+[root.val])
        :
