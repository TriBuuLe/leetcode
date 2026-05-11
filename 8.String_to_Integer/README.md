# 8. String to Integer (atoi)

## Problem

Implement the `myAtoi(string s)` function, which converts a string to a **32-bit signed integer**.

The algorithm works as follows:

1. **Whitespace**  
   Ignore any leading whitespace (`" "`).

2. **Signedness**  
   Determine the sign by checking if the next character is `'-'` or `'+'`.  
   Assume positive if neither is present.

3. **Conversion**  
   Read digits and build the number until a non-digit character is encountered or the string ends.  
   If no digits are read, return `0`.

4. **Rounding**  
   Clamp the result to the 32-bit signed integer range:
   ```text
   [-2^31, 2^31 - 1]
   ```

Return the final integer.

---

## Examples

### Example 1

```text
Input: s = "42"
Output: 42
```

---

### Example 2

```text
Input: s = "   -042"
Output: -42
```

---

### Example 3

```text
Input: s = "1337c0d3"
Output: 1337
```

---

### Example 4

```text
Input: s = "0-1"
Output: 0
```

---

### Example 5

```text
Input: s = "words and 987"
Output: 0
```

---

## Constraints

```text
0 <= s.length <= 200
s consists of English letters, digits (0-9), ' ', '+', '-', and '.'
```