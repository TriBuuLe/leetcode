# 10. Regular Expression Matching

## Problem

Given an input string `s` and a pattern `p`, implement regular expression matching with support for:

- `.` Matches **any single character**
- `*` Matches **zero or more of the preceding element**

The matching must cover the **entire string** (not partial).

---

## Examples

### Example 1

```text
Input: s = "aa", p = "a"
Output: false
```

### Explanation

```text
"a" does not match the entire string "aa"
```

---

### Example 2

```text
Input: s = "aa", p = "a*"
Output: true
```

### Explanation

```text
'*' means zero or more of the preceding element 'a'
"a*" → "aa"
```

---

### Example 3

```text
Input: s = "ab", p = ".*"
Output: true
```

### Explanation

```text
".*" means zero or more of any character
```

---

## Constraints

```text
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters
p contains only lowercase English letters, '.', and '*'
'*' will always have a valid preceding character
```