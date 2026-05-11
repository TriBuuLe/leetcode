# 12. Integer to Roman

## Problem

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending values from **highest to lowest**.

### Rules

- If the value does **not** start with 4 or 9:
  - Append the largest possible symbol
  - Subtract its value
  - Repeat

- If the value **starts with 4 or 9**, use subtractive notation:
  ```text
  4   → IV
  9   → IX
  40  → XL
  90  → XC
  400 → CD
  900 → CM
  ```

- Only `I`, `X`, `C`, `M` can repeat up to 3 times
- `V`, `L`, `D` cannot be repeated

Given an integer `num`, convert it to a Roman numeral.

---

## Examples

### Example 1

```text
Input: num = 3749
Output: "MMMDCCXLIX"
```

### Explanation

```text
3000 = MMM
 700 = DCC
  40 = XL
   9 = IX
```

---

### Example 2

```text
Input: num = 58
Output: "LVIII"
```

### Explanation

```text
50 = L
 8 = VIII
```

---

### Example 3

```text
Input: num = 1994
Output: "MCMXCIV"
```

### Explanation

```text
1000 = M
 900 = CM
  90 = XC
   4 = IV
```

---

## Constraints

```text
1 <= num <= 3999
```