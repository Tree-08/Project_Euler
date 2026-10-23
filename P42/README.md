# Problem 42 — Coded Triangle Numbers

[Problem link](https://projecteuler.net/problem=42)

The *word value* of a word is the sum of its letters' alphabetical positions (A=1, B=2, …). Using a file of 1786 common English words, count how many have a word value that is a triangle number (`tₙ = n(n+1)/2`).

## Approach

For each word, compute its value, then test whether it is triangular.

**Triangle test.** A number `t` is triangular if `t = n(n+1)/2` for some positive integer `n`. Rearranging gives `n² + n − 2t = 0`, whose positive root is

```
n = (√(8t + 1) − 1) / 2
```

which is an integer exactly when `8t + 1` is a perfect square. The code checks this with `math.isqrt`, which works in exact integer arithmetic, so there is no floating-point error.

**Parsing.** The file is one line of comma-separated, double-quoted words. After splitting on commas, each word is lower-cased and only the letters `a`–`z` are counted, which ignores the quotes.

## Complexity

O(total characters) with an O(1) test per word.

## Run

`words.txt` is read from the current directory, so run it from this folder.

```
cd P42
python P42.py
```

## Files

- `P42.py` — solution
- `words.txt` — input data from Project Euler

## Answer

`162`
