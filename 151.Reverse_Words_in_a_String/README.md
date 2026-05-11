# 151. Reverse Words in a String

## Problem

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters.

Return a string of the words in reverse order concatenated by a single space.

The returned string should not contain leading or trailing spaces, and multiple spaces between words should be reduced to a single space.

## Examples

### Example 1

```text
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### Explanation

```text
Reverse the order of the words.
```

---

### Example 2

```text
Input: s = "  hello world  "
Output: "world hello"
```

### Explanation

```text
Remove leading/trailing spaces and reverse words.
```

---

### Example 3

```text
Input: s = "a good   example"
Output: "example good a"
```

### Explanation

```text
Reduce multiple spaces to one and reverse words.
```

---

## Constraints

```text
1 <= s.length <= 10^4
s contains English letters, digits, and spaces ' '.
There is at least one word in s.
```