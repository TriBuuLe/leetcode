# 134. Gas Station

## Problem

There are `n` gas stations along a circular route.

- `gas[i]` is the amount of gas at station `i`
- `cost[i]` is the gas needed to travel from station `i` to station `i + 1`

You have a car with an unlimited gas tank and start with an empty tank at one of the gas stations.

Return the starting gas station index if you can travel around the circuit once clockwise. Otherwise, return `-1`.

If a solution exists, it is guaranteed to be unique.

## Examples

### Example 1

```text
Input: gas = [1,2,3,4,5]
       cost = [3,4,5,1,2]

Output: 3
```

### Explanation

```text
Start at station 3:

Tank = 0 + 4 = 4
Travel to station 4:
Tank = 4 - 1 + 5 = 8

Travel to station 0:
Tank = 8 - 2 + 1 = 7

Travel to station 1:
Tank = 7 - 3 + 2 = 6

Travel to station 2:
Tank = 6 - 4 + 3 = 5

Travel back to station 3:
Tank = 5 - 5 = 0

Successfully completed the circuit.
```

---

### Example 2

```text
Input: gas = [2,3,4]
       cost = [3,4,3]

Output: -1
```

### Explanation

```text
No starting station allows completing the full circuit.
```

---

## Constraints

```text
n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4
The answer is guaranteed to be unique.
```