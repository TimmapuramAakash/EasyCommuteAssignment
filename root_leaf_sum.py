# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    solutions = []
    def pathSumUtil(self, root, req_sum, current_path ):
        if root==None:
            return
        current_path.append(root.val)
        # print(current_path)
        if root.left==None and root.right ==None:
            if req_sum == root.val:
                self.solutions.append(current_path)
                # print(current_path,self.solutions)
                return
            else:
                return
        self.pathSumUtil(root.left,req_sum-root.val,list(current_path))
        self.pathSumUtil(root.right,req_sum-root.val,list(current_path))
        
            
    def pathSum(self, A, B):
        dummy = []
        self.solutions = []
        self.pathSumUtil(A,B,list(dummy))
        return self.solutions
