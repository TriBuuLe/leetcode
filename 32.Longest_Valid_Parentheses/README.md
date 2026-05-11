# 32. Longest Valid Parentheses

## Problem

Given a string containing just the characters `'('` and `')'`, return the length of the longest valid parentheses substring.

A valid parentheses substring is one where every opening parenthesis has a matching closing parenthesis in the correct order.

## Examples

### Example 1

```text
Input: s = "(()"
Output: 2
```

### Explanation

```text
The longest valid parentheses substring is "()".
```

---

### Example 2

```text
Input: s = ")()())"
Output: 4
```

### Explanation

```text
The longest valid parentheses substring is "()()".
```

---

### Example 3

```text
Input: s = ""
Output: 0
```

### Explanation

```text
The string is empty, so there is no valid parentheses substring.
```

---

## Constraints

```text
0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
```