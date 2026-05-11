# 380. Insert Delete GetRandom O(1)

## Problem

Implement the `RandomizedSet` class:

- `RandomizedSet()` initializes the object.
- `bool insert(int val)` inserts an item into the set if not present.
  - Returns `true` if the item was inserted.
  - Returns `false` if it already existed.
- `bool remove(int val)` removes an item from the set if present.
  - Returns `true` if the item existed.
  - Returns `false` otherwise.
- `int getRandom()` returns a random element from the current set.
  - Each element must have the same probability of being returned.

All functions must work in average **O(1)** time complexity.

## Examples

### Example 1

```text
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]

[[], [1], [2], [2], [], [1], [2], []]

Output:
[null, true, false, true, 2, true, false, 2]
```

### Explanation

```text
RandomizedSet randomizedSet = new RandomizedSet();

randomizedSet.insert(1);
Returns true because 1 was inserted.

randomizedSet.remove(2);
Returns false because 2 does not exist.

randomizedSet.insert(2);
Returns true. Set is now [1,2].

randomizedSet.getRandom();
Returns either 1 or 2 randomly.

randomizedSet.remove(1);
Returns true. Set is now [2].

randomizedSet.insert(2);
Returns false because 2 already exists.

randomizedSet.getRandom();
Returns 2 because it is the only element.
```

---

## Constraints

```text
-2^31 <= val <= 2^31 - 1

At most 2 * 10^5 calls will be made to
insert, remove, and getRandom.

There will be at least one element in the
data structure when getRandom is called.
```