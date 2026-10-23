# Problem 23 — Non-Abundant Sums

[Problem link](https://projecteuler.net/problem=23)

A number is *abundant* if the sum of its proper divisors exceeds the number. Every integer greater than 28123 can be written as the sum of two abundant numbers. Find the sum of all positive integers that **cannot** be written as the sum of two abundant numbers.

## Approach

1. **Sieve the proper-divisor sums** `d[n]` for `n ≤ 28123`, exactly as in [P21](../P21): for each `i`, add `i` to `d[j]` for `j = 2i, 3i, …`.
2. **Mark the sums.** For each abundant `i` (where `d[i] > i`), pair it with every `j ≤ i` that is also abundant, and mark `i + j` in the `temp` array when it is within range. Only pairs with `j ≤ i` are needed because addition is commutative.
3. **Add up the unmarked numbers** in `1 … 28123`.

## Complexity

The sieve is O(N log N). The marking step runs its inner loop over every `j ≤ i` for each abundant `i`, so it is roughly O(N · A), where `A` (6965) is the number of abundant numbers up to `N`. It finishes in about 5 seconds in CPython.

A faster version would first collect the abundant numbers into a list and iterate only over that list, breaking as soon as the sum exceeds `N`.

## Run

```
python P23.py
```

## Answer

`4179871`
