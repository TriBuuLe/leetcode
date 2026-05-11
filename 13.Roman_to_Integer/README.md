# 13. Roman to Integer

## Problem

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written from **largest to smallest from left to right**.

However, in some cases, subtraction is used:

```text
I before V or X   → 4 (IV), 9 (IX)
X before L or C   → 40 (XL), 90 (XC)
C before D or M   → 400 (CD), 900 (CM)
```

Given a Roman numeral string `s`, convert it to an integer.

---

## Examples

### Example 1

```text
Input: s = "III"
Output: 3
```

### Explanation

```text
I + I + I = 3
```

---

### Example 2

```text
Input: s = "LVIII"
Output: 58
```

### Explanation

```text
L = 50, V = 5, III = 3 → 50 + 5 + 3 = 58
```

---

### Example 3

```text
Input: s = "MCMXCIV"
Output: 1994
```

### Explanation

```text
M = 1000
CM = 900
XC = 90
IV = 4
Total = 1994
```

---

## Constraints

```text
1 <= s.length <= 15
s contains only ('I', 'V', 'X', 'L', 'C', 'D', 'M')
s is guaranteed to be a valid Roman numeral in [1, 3999]
```