# 20. Valid Parentheses

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.  
Open brackets must be closed in the correct order.  
Every close bracket has a corresponding open bracket of the same type.

## Examples

### Example 1

```text
Input: s = "()"
Output: true
```

### Explanation

```text
The parentheses are correctly matched and ordered.
```

---

### Example 2

```text
Input: s = "()[]{}"
Output: true
```

### Explanation

```text
Each type of bracket is properly opened and closed in the correct order.
```

---

### Example 3

```text
Input: s = "(]"
Output: false
```

### Explanation

```text
The opening '(' is closed by ']', which is not the same type.
```

---

### Example 4

```text
Input: s = "([])"
Output: true
```

### Explanation

```text
The brackets are correctly nested and matched.
```

---

### Example 5

```text
Input: s = "([)]"
Output: false
```

### Explanation

```text
The brackets are not closed in the correct order.
```

---

## Constraints

```text
1 <= s.length <= 10^4
s consists only of the characters '()[]{}'
```