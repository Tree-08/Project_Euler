# Problem 19 — Counting Sundays

[Problem link](https://projecteuler.net/problem=19)

Count how many months between 1 Jan 1901 and 31 Dec 2000 began on a Sunday.

## Approach

Track the weekday of the 1st of each month as a number mod 7, with `0 = Sunday`.

- `curr` starts at `6` (Saturday), the weekday of 1 Dec 1900. 1 Jan 1900 was a Monday and 1900 was not a leap year, so 1 Jan 1901 was a Tuesday, and 31 days earlier (31 mod 7 = 3) is a Saturday.
- Moving from the 1st of one month to the 1st of the next shifts the weekday by the length of the *previous* month, mod 7. The `days` array is therefore offset by one: `days[0]` is December's length (31 → 3), `days[1]` is January's, and so on. February contributes `28 mod 7 = 0`.
- In a leap year, March gets an extra `+1` (the 29th of February). Testing `yr % 4 == 0` is enough here, because 2000 is the only century year in range and it is a leap year.
- After each step `curr` is the weekday of the 1st of month `mn` in year `yr`; count the times it is `0`.

## Complexity

O(years × 12) — trivial.

## Run

```
python P19.py
```

## Answer

`171`
