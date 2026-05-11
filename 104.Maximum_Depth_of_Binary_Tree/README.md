# 104. Maximum Depth of Binary Tree

## Problem

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

### Example 1

```text
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Explanation

```text
The longest path is 3 -> 20 -> 15 (or 7), which has 3 nodes.
```

---

### Example 2

```text
Input: root = [1,null,2]
Output: 2
```

### Explanation

```text
The longest path is 1 -> 2, which has 2 nodes.
```

---

## Constraints

```text
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
```