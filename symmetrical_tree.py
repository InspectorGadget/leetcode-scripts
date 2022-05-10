#
#
# @author InspectorGadget (https://github.com/InspectorGadget)
# LeetCode: Symmetrical Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
# Guide:
# - Tree with the range of [1, 100]
# - Formula: -100 <= Node.val <= 100
#
# Time complexity: O(n)
# Space complexity: O(n)
#
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SymmetrialTree:
    """
        @return (bool)
    """
    def isSymmetrical(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    """
        @return (bool)
    """
    def isMirror(self, one, two) -> bool:
        if not one and not two: return True
        if not one or not two: return False
        return (
            one.val == two.val and
            self.isMirror(one.right, two.left) and
            self.isMirror(one.left, two.right)
        )