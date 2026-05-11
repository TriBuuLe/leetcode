# 9. Palindrome Number

## Problem

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a palindrome when it reads the same forward and backward.

---

## Examples

### Example 1

```text
Input: x = 121
Output: true
```

### Explanation

```text
121 reads the same from left to right and right to left.
```

---

### Example 2

```text
Input: x = -121
Output: false
```

### Explanation

```text
From left to right: -121
From right to left: 121-
Not the same → not a palindrome
```

---

### Example 3

```text
Input: x = 10
Output: false
```

### Explanation

```text
From right to left: 01
Not the same → not a palindrome
```

---

## Constraints

```text
-2^31 <= x <= 2^31 - 1
```

---

## Follow-up

- Can you solve it **without converting the integer to a string**?