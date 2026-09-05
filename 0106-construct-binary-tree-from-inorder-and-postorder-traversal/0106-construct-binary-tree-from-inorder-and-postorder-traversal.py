# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        return self.construct_tree_from_inorder_and_Postorder(inorder, postorder,0, n-1, 0, n-1)
    def construct_tree_from_inorder_and_Postorder(self,inorder,postorder,ins,ine,pos,poe):

        if (ins>ine or pos>poe):
            return None
        root_data=postorder[poe]

        root=TreeNode(root_data)

        rootIndexInorder=-1

        for i in range(ins,ine+1):

            if (inorder[i]==root_data):
                rootIndexInorder=i
                break

        if (rootIndexInorder==-1):
            print("root not found in inorder, plz check")
            return None
        lins=ins
        line=rootIndexInorder-1
        lpos= pos
        lpoe=pos+(line-lins)

        rins=rootIndexInorder+1
        rine=ine
        rpos=lpoe+1
        rpoe=poe-1

        root.left=self.construct_tree_from_inorder_and_Postorder(inorder, postorder,lins, line,lpos,lpoe)
        root.right=self.construct_tree_from_inorder_and_Postorder(inorder, postorder,rins, rine, rpos,rpoe)

        return root
    
        