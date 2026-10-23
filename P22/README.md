# Problem 22 — Names Scores

[Problem link](https://projecteuler.net/problem=22)

Given a file of 5163 first names, sort them alphabetically. A name's score is its alphabetical value (A=1, B=2, …) multiplied by its 1-based position in the sorted list. Find the total of all scores.

## Approach

1. Read `names.txt`, split on commas and strip the surrounding double quotes.
2. Sort the list; Python's default string ordering is alphabetical for upper-case names.
3. For the name at 0-based index `j`, add `(sum of letter values) × (j + 1)` to the running total. A letter's value is `ord(c) − ord('A') + 1`.

## Complexity

O(n log n) for the sort plus O(total characters) for scoring.

## Run

`names.txt` is read from the current directory, so run it from this folder.

```
cd P22
python P22.py
```

## Files

- `P22.py` — solution
- `names.txt` — input data from Project Euler

## Answer

`871198282`
