# 55. Jump Game

## Problem

You are given an integer array `nums`.

You are initially positioned at the array's first index, and each element in the array represents your **maximum jump length** at that position.

Return `true` if you can reach the last index, or `false` otherwise.

## Examples

### Example 1

```text
Input: nums = [2,3,1,1,4]
Output: true
```

### Explanation

```text
Jump 1 step from index 0 to index 1.
Then jump 3 steps from index 1 to the last index.
```

---

### Example 2

```text
Input: nums = [3,2,1,0,4]
Output: false
```

### Explanation

```text
You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.
```

---

## Constraints

```text
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
```