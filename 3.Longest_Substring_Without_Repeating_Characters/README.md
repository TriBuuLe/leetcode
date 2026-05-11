# 3. Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the **longest substring** without duplicate characters.

A **substring** is a contiguous sequence of characters within a string.

---

## Examples

### Example 1

```text
Input: s = "abcabcbb"
Output: 3
```

### Explanation

```text
The answer is "abc", with length 3.
Other valid substrings include "bca" and "cab".
```

---

### Example 2

```text
Input: s = "bbbbb"
Output: 1
```

### Explanation

```text
The answer is "b", with length 1.
```

---

### Example 3

```text
Input: s = "pwwkew"
Output: 3
```

### Explanation

```text
The answer is "wke", with length 3.
Note: "pwke" is a subsequence, not a substring.
```

---

## Constraints

```text
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols, and spaces
```