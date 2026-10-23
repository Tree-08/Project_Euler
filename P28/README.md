# Problem 28 — Number Spiral Diagonals

[Problem link](https://projecteuler.net/problem=28)

Numbers are written in a clockwise spiral starting from 1 in the centre of a grid. What is the sum of the numbers on both diagonals of a 1001 × 1001 spiral?

## Approach

The spiral is built from square rings. The ring with side length `i` (odd, `i ≥ 3`) ends at `i²` in one corner, and the other three corners are each `i − 1` less than the previous one:

```
i²,  i² − (i−1),  i² − 2(i−1),  i² − 3(i−1)
```

Their sum is

```
4i² − 6(i − 1)
```

Start with `1` for the centre and add this expression for `i = 3, 5, 7, …, 1001`.

For example, `i = 3` contributes `4·9 − 12 = 24` (3 + 5 + 7 + 9), so the 3×3 spiral has diagonal sum `1 + 24 = 25`.

## Complexity

O(N) for a side length `N`; a closed form in terms of sums of squares also exists, but the loop is only 500 iterations.

## Run

```
python P28.py
```

## Answer

`669171001`
