# 122. Best Time to Buy and Sell Stock II

## Problem

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.

You may sell and buy the stock multiple times on the same day, as long as you never hold more than one share of the stock.

Find and return the **maximum profit** you can achieve.

## Examples

### Example 1

```text
Input: prices = [7,1,5,3,6,4]
Output: 7
```

### Explanation

```text
Buy on day 2 at price 1 and sell on day 3 at price 5.
Profit = 5 - 1 = 4

Then buy on day 4 at price 3 and sell on day 5 at price 6.
Profit = 6 - 3 = 3

Total profit = 4 + 3 = 7
```

---

### Example 2

```text
Input: prices = [1,2,3,4,5]
Output: 4
```

### Explanation

```text
Buy on day 1 at price 1 and sell on day 5 at price 5.
Profit = 5 - 1 = 4
```

---

### Example 3

```text
Input: prices = [7,6,4,3,1]
Output: 0
```

### Explanation

```text
There is no way to make a positive profit, so we never buy the stock.
Maximum profit = 0
```

---

## Constraints

```text
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
```