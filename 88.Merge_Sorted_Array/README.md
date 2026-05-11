# 88. Merge Sorted Array

## Problem

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should be stored inside `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the valid elements, and the last `n` elements are set to 0 and should be ignored.

## Examples

### Example 1

```text
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

### Explanation

```text
Merge [1,2,3] and [2,5,6] into nums1.
```

---

### Example 2

```text
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

### Explanation

```text
nums2 is empty, so nums1 remains unchanged.
```

---

### Example 3

```text
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

### Explanation

```text
nums1 has no valid elements, so result is nums2.
```

---

## Constraints

```text
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
```