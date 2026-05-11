# 49. Group Anagrams

## Problem

Given an array of strings `strs`, group the anagrams together.

You can return the answer in any order.

## Examples

### Example 1

```text
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

### Explanation

```text
"nat" and "tan" are anagrams.
"ate", "eat", and "tea" are anagrams.
"bat" has no matching anagram.
```

---

### Example 2

```text
Input: strs = [""]
Output: [[""]]
```

### Explanation

```text
Single empty string forms its own group.
```

---

### Example 3

```text
Input: strs = ["a"]
Output: [["a"]]
```

### Explanation

```text
Single character string forms its own group.
```

---

## Constraints

```text
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
```