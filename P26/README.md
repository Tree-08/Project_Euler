# Problem 26 — Reciprocal Cycles

[Problem link](https://projecteuler.net/problem=26)

Find the value of `d < 1000` for which `1/d` has the longest recurring cycle in its decimal fraction part.

## Approach

Simulate long division of `1/d`. The state at each step is the current remainder, and there are fewer than `d` possible remainders, so a remainder must eventually repeat.

For each `i` in `2 … 999`:

1. Start with `temp = 10` (the remainder 1, shifted one digit).
2. Compute `r = temp % i`.
   - If `r == 0`, the decimal terminates, so there is no cycle.
   - If `r` was already seen at step `s[r]`, the cycle length is `step − s[r]`.
   - Otherwise record `s[r] = step` and continue with `temp = 10 · r`.
3. Keep the `i` with the largest cycle length.

The program prints the longest cycle length (`982`) and then the `d` that produces it.

## The number-theory view

The code also notes why this works. Strip every factor of 2 and 5 from `d` to get `d'`. Those factors only affect the non-repeating prefix. The cycle length is the smallest `k` with `10ᵏ ≡ 1 (mod d')`, the multiplicative order of 10, which divides Euler's totient `φ(d')`. The longest possible cycle for a prime `p` is `p − 1`, reached when 10 is a primitive root mod `p` (a "full reptend prime"). `983` is such a prime, and its cycle length is `982 = 983 − 1`.

## Complexity

O(D²) in the worst case for the limit `D = 1000`, since each `i` runs at most `i` steps. It runs in well under a second.

## Run

```
python P26.py
```

## Answer

`983` (cycle length 982)
