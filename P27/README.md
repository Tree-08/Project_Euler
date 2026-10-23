# Problem 27 — Quadratic Primes

[Problem link](https://projecteuler.net/problem=27)

Consider `n² + an + b` with `|a| < 1000` and `|b| ≤ 1000`. Find the product `a·b` for the polynomial that produces the most consecutive primes, starting from `n = 0`.

## Approach

Brute force over `(a, b)`, using a sieve for primality and a few observations to shrink the search space.

**Pruning**

- `n = 0` gives `b`, so `b` must be prime (and positive).
- Euler's polynomial `n² + n + 41` already yields 40 primes (`n = 0 … 39`), so a better one must beat that.
- At `n = b` the value is `b² + ab + b = b(b + a + 1)`, which is divisible by `b` and therefore composite. A polynomial can produce at most `b` consecutive primes, so `b ≥ 41` is required.
- Then `b` is an odd prime, and `n = 1` gives `1 + a + b`, which must be prime. It cannot be 2, since that would force `a = 1 − b` and make `f(2) = 6 − b` negative. So it is odd, which makes `a` odd.

So the search covers odd `a` in `[−999, 999]` and odd `b` in `[41, 1000]`, skipping any `b` that is not prime.

**Primality**

A sieve of Eratosthenes up to 2,000,000 covers the largest value that can come up (about `999² + 999·999 + 1000 ≈ 2·10⁶`), and any polynomial value `≤ 1` is treated as non-prime.

**Counting**

For each candidate, step `x = 0, 1, 2, …` until `f(x)` fails. The loop tracks `x − 1`, the last `n` for which every value so far was prime, so the printed `70` means primes for `n = 0 … 70`, i.e. **71** consecutive primes. The program prints that value, then `a`, `b` and `a·b`.

The winner is `n² − 61n + 971`.

## Complexity

About 1000 × 480 candidate pairs, each stopping at its first composite, plus an O(N log log N) sieve. It runs in roughly 0.3 s.

## Run

```
python P27.py
```

## Answer

`-59231` (`a = −61`, `b = 971`)
