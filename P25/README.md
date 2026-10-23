# Problem 25 — 1000-digit Fibonacci Number

[Problem link](https://projecteuler.net/problem=25)

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

## Approach

Generate the sequence with Python's arbitrary-precision integers and watch the digit count.

- The list starts as `[0, 1]`, so `l[k] = F(k)` and the index of the newest term is `len(l) − 1`.
- `curr` is the digit count of the previous term. When a new term has a different digit count, the count has gone up by exactly one (consecutive Fibonacci numbers differ by less than a factor of 10). If `curr + 1 == 1000`, this is the first 1000-digit term, so print its index.
- `N = 10000` is only a safety cap on the loop.

## Cross-check with Binet's formula

`F(n) ≈ φⁿ / √5`, so `F(n) ≥ 10⁹⁹⁹` when

```
n ≥ (999 + log10(√5)) / log10(φ) ≈ 4781.86
```

The smallest integer is `4782`, matching the simulation.

## Complexity

About 4800 big-integer additions; the numbers have up to 1000 digits, so the cost is O(n · digits).

## Run

```
python P25.py
```

## Answer

`4782`
