# 238. Product of Array Except Self

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

You must write an algorithm that runs in **O(n)** time and does not use the division operation.

## Examples

### Example 1

```text
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Explanation

```text
For each index, multiply every number except the number at that index.
```

---

### Example 2

```text
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

### Explanation

```text
Only the index with value 0 gets the product of all non-zero elements.
All other indexes include the 0 in their product, so they become 0.
```

---

## Constraints

```text
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The answer is guaranteed to fit in a 32-bit integer.
```