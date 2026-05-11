# 125. Valid Palindrome

## Problem

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

### Example 1

```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

### Explanation

```text
After cleaning: "amanaplanacanalpanama" → same forward and backward.
```

---

### Example 2

```text
Input: s = "race a car"
Output: false
```

### Explanation

```text
After cleaning: "raceacar" → not a palindrome.
```

---

### Example 3

```text
Input: s = " "
Output: true
```

### Explanation

```text
After removing non-alphanumeric characters: "" (empty string), which is a palindrome.
```

---

## Constraints

```text
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
```