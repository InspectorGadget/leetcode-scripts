#
#
# @author InspectorGadget (https://github.com/InspectorGadget)
# LeetCode: Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Guide:
# - Tree with the range of [0, 104]
# - Formula: -100 <= Node.val <= 100
#
# Time complexity: O(n)
# Space complexity: O(Log (n))
#
#

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaximumBinaryTreeDepth:
    def calculateMaxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # Unpack values to variables
        (
            left, 
            right
        ) = (
            self.calculateMaxDepth(root.left), 
            self.calculateMaxDepth(root.right)
        )

        # Prepend 1 to the max of left and right
        return max(left, right) + 1

