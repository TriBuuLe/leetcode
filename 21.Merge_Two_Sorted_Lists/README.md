# 21. Merge Two Sorted Lists

## Problem

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Examples

### Example 1

```text
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Explanation

```text
Merge both lists by always taking the smaller current node.
```

---

### Example 2

```text
Input: list1 = [], list2 = []
Output: []
```

### Explanation

```text
Both lists are empty, so return an empty list.
```

---

### Example 3

```text
Input: list1 = [], list2 = [0]
Output: [0]
```

### Explanation

```text
One list is empty, so return the other list.
```

---

## Constraints

```text
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
```