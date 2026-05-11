# 274. H-Index

## Problem

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`th paper, return the researcher's **h-index**.

The h-index is defined as the maximum value of `h` such that the researcher has published at least `h` papers that have each been cited at least `h` times.

## Examples

### Example 1

```text
Input: citations = [3,0,6,1,5]
Output: 3
```

### Explanation

```text
There are 3 papers with at least 3 citations each.
```

---

### Example 2

```text
Input: citations = [1,3,1]
Output: 1
```

### Explanation

```text
There is only 1 paper with at least 1 citation.
```

---

## Constraints

```text
n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
```