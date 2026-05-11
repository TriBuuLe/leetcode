# 15. 3Sum

## Problem

Given an integer array `nums`, return all the triplets:

```text
[nums[i], nums[j], nums[k]]
```

such that:

```text
i != j
i != k
j != k
nums[i] + nums[j] + nums[k] == 0
```

The solution set must not contain duplicate triplets.

---

## Examples

### Example 1

```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

### Explanation

```text
The distinct triplets that sum to 0 are:
[-1,-1,2]
[-1,0,1]

The order of the output and the order of the triplets does not matter.
```

---

### Example 2

```text
Input: nums = [0,1,1]
Output: []
```

### Explanation

```text
The only possible triplet does not sum to 0.
```

---

### Example 3

```text
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

### Explanation

```text
The only possible triplet sums to 0.
```

---

## Constraints

```text
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
```