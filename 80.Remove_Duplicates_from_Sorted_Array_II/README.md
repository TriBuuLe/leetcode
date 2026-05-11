# 80. Remove Duplicates from Sorted Array II

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.

The relative order of the elements should be kept the same.

Return `k` such that the first `k` elements of `nums` contain the final result. It does not matter what you leave beyond the first `k` elements.

You must do this in-place with **O(1)** extra memory.

## Examples

### Example 1

```text
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

### Explanation

```text
Each number can appear at most twice.
```

---

### Example 2

```text
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

### Explanation

```text
Extra duplicates beyond two are removed.
```

---

## Constraints

```text
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
```