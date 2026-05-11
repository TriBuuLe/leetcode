# 6. Zigzag Conversion

## Problem

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows.

For example, with `numRows = 3`:

```text
P   A   H   N
A P L S I I G
Y   I   R
```

Reading line by line gives:

```text
PAHNAPLSIIGYIR
```

Write a function that takes a string `s` and an integer `numRows`, then returns the zigzag conversion.

---

## Examples

### Example 1

```text
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

---

### Example 2

```text
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
```

### Explanation

```text
P     I    N
A   L S  I G
Y A   H R
P     I
```

---

### Example 3

```text
Input: s = "A", numRows = 1
Output: "A"
```

---

## Constraints

```text
1 <= s.length <= 1000
s consists of English letters, ',' and '.'
1 <= numRows <= 1000
```