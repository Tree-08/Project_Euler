# Problem 30 — Digit Fifth Powers

[Problem link](https://projecteuler.net/problem=30)

Find the sum of all numbers that can be written as the sum of the fifth powers of their digits. (`1 = 1⁵` is not a sum, so it is excluded.)

## Approach

**Upper bound.** A `d`-digit number's digit-power sum is at most `d · 9⁵ = 59049·d`. For `d = 7` that is 413343, which has too few digits to be a 7-digit number (≥ 1,000,000), and the gap only widens for larger `d`. So no solution has 7 or more digits, and it is enough to search up to `6 · 9⁵ = 354294`.

The comment in the code notes that this can be tightened. Any 6-digit solution is at most 354294, so its leading digit is at most 3. A leading 3 would need a digit-power sum of at least 300000, but the most it can reach is `3⁵ + 5·9⁵ = 295488`. So the leading digit is at most 2, and the largest possible sum is then `2⁵ + 5·9⁵ = 295277`. That makes `295277` a sufficient bound.

**Search.** For each `i` from 10 upward (single digits are skipped because a one-digit number is not a *sum*), `chk` peels off the digits with `% 10` and `/ 10`, adds up their fifth powers, and compares with `i`. The matches are summed.

The numbers found are 4150, 4151, 54748, 92727, 93084 and 194979.

## Complexity

O(limit · digits) — a few million operations.

## Run

The program reads the search limit `n` from standard input. Any value of at least `354294` gives the right answer.

```
g++ -O2 -o P30 P30.cpp
echo 354294 | ./P30
```

## Answer

`443839`
