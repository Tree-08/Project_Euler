# Problem 6 — Sum Square Difference

[Problem link](https://projecteuler.net/problem=6)

Find the difference between the square of the sum and the sum of the squares of the first `n` natural numbers (here `n = 100`).

## Approach

No loop is needed. Both quantities have closed forms:

- Square of the sum: `(n(n+1)/2)² = n²(n+1)²/4`
- Sum of the squares: `n(n+1)(2n+1)/6`

Subtracting and putting everything over 12:

```
n²(n+1)²/4 − n(n+1)(2n+1)/6
  = n(n+1)·[3n(n+1) − 2(2n+1)] / 12
  = n(n+1)(3n² − n − 2) / 12
  = n(n+1)(n−1)(3n+2) / 12
```

The code evaluates `(n−1)·n/2`, then multiplies by `(n+1)` and divides by 3, then multiplies by `(3n+2)` and divides by 2. Each intermediate division is exact, so integer arithmetic gives the right answer.

## Complexity

O(1) time and memory.

## Run

The program reads `n` from standard input.

```
g++ -O2 -o P6 P6.cpp
echo 100 | ./P6
```

## Answer

`25164150`
