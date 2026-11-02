/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true;
        }
        if ((root == null && subRoot != null)
            || (root != null && subRoot == null)) {
                return false;
            }
        if (root.val == subRoot.val) {
            if(this.isSubtree(root.left, subRoot.left) 
               && this.isSubtree(subRoot.right, subRoot.right)) {
                return true;
            }
        }
        return this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot);
    }
}
