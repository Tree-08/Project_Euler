# Problem 24 — Lexicographic Permutations

[Problem link](https://projecteuler.net/problem=24)

What is the millionth lexicographic permutation of the digits 0–9?

## Approach

Use the factorial number system instead of generating permutations.

There are `9! = 362880` permutations that start with any given first digit, so the first digit is determined by `idx // 9!`. Fixing it leaves `9` digits and a new index `idx % 9!`, and the same step repeats with `8!`, `7!`, and so on.

1. Precompute `fact[k] = k!`.
2. Convert the 1-based rank to a 0-based index: `idx = 1_000_000 − 1`.
3. While digits remain, with `m` of them left in the sorted list `l`:
   - `q = idx // fact[m − 1]` picks the next digit, `l[q]`.
   - `idx %= fact[m − 1]`.
   - Append the digit to the answer and remove it from `l`.

The list `l` stays sorted, so index `q` really is the `q`-th smallest remaining digit.

## Complexity

O(N²) for `N` digits because of `list.remove`, which is negligible for `N = 10`.

## Run

```
python P24.py
```

## Answer

`2783915460`
