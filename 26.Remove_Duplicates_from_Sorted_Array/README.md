# 26. Remove Duplicates from Sorted Array

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

The relative order of the elements should be kept the same.

Return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in sorted order. The remaining elements beyond index `k - 1` can be ignored.

## Examples

### Example 1

```text
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

### Explanation

```text
The function returns k = 2, and the first two elements are 1 and 2.
```

---

### Example 2

```text
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

### Explanation

```text
The function returns k = 5, and the first five elements are 0, 1, 2, 3, 4.
```

---

## Constraints

```text
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
```