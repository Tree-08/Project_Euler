# Problem 21 — Amicable Numbers

[Problem link](https://projecteuler.net/problem=21)

Let `d(n)` be the sum of the proper divisors of `n` (divisors less than `n`). If `d(a) = b`, `d(b) = a` and `a ≠ b`, then `a` and `b` are an amicable pair. Sum all amicable numbers under 10000.

## Approach

1. **Sieve `d(n)` for every `n ≤ N`.** For each `i` from 1 to `N/2`, add `i` to `d[j]` for every multiple `j = 2i, 3i, …`. Starting at `2i` (not `i`) is what excludes the number itself, so `d[j]` ends up as the sum of *proper* divisors.
2. **Check each `i`.** It is amicable when `d[d[i]] == i` and `d[i] != i` (the second condition removes perfect numbers such as 6 and 28). The `d[i] <= N` guard keeps the `d[d[i]]` lookup inside the array.
3. Sum the amicable numbers.

The pairs found are (220, 284), (1184, 1210), (2620, 2924), (5020, 5564) and (6232, 6368).

## Complexity

The sieve is O(N log N) (harmonic sum), with O(N) memory.

## Run

```
python P21.py
```

## Answer

`31626`
