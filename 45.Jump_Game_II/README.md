# 45. Jump Game II

## Problem

You are given a **0-indexed** array of integers `nums` of length `n`.

You are initially positioned at index `0`.

Each element `nums[i]` represents the **maximum length of a forward jump** from index `i`.  
In other words, if you are at index `i`, you can jump to any index `(i + j)` where:

- `0 <= j <= nums[i]`, and  
- `i + j < n`

Return the **minimum number of jumps** required to reach index `n - 1`.

It is guaranteed that you can reach the last index.

---

## Examples

### Example 1

```text
Input: nums = [2,3,1,1,4]
Output: 2
```

### Explanation

```text
Jump 1 step from index 0 to index 1.
Then jump 3 steps from index 1 to the last index.
Total jumps = 2
```

---

### Example 2

```text
Input: nums = [2,3,0,1,4]
Output: 2
```

---

## Constraints

```text
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
```

---

## Notes

- It is guaranteed that you can reach the last index.
- You must return the **minimum number of jumps**.