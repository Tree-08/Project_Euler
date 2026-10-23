# Project Euler Solutions

My solutions to [Project Euler](https://projecteuler.net) problems, in Python and C++.

Each problem lives in its own folder named `P<number>` (for example `P12` for problem 12). A folder contains the solution code and a `README.md` that explains the approach, its complexity and how to run it.

## Solved problems

| # | Problem | Language | Answer |
|---|---------|----------|--------|
| 6 | [Sum Square Difference](P6) | C++ | 25164150 |
| 19 | [Counting Sundays](P19) | Python | 171 |
| 21 | [Amicable Numbers](P21) | Python | 31626 |
| 22 | [Names Scores](P22) | Python | 871198282 |
| 23 | [Non-Abundant Sums](P23) | Python | 4179871 |
| 24 | [Lexicographic Permutations](P24) | Python | 2783915460 |
| 25 | [1000-digit Fibonacci Number](P25) | Python | 4782 |
| 26 | [Reciprocal Cycles](P26) | Python | 983 |
| 27 | [Quadratic Primes](P27) | Python | -59231 |
| 28 | [Number Spiral Diagonals](P28) | Python | 669171001 |
| 29 | [Distinct Powers](P29) | Python | 9183 |
| 30 | [Digit Fifth Powers](P30) | C++ | 443839 |
| 42 | [Coded Triangle Numbers](P42) | Python | 162 |

## Layout

```
P<n>/
├── P<n>.py | P<n>.cpp   solution code
├── README.md            explanation of the solution
└── *.txt                input data, only where the problem needs it (P22, P42)
```

## Running a solution

**Python** (3.8+)

```
cd P19
python P19.py
```

Run from inside the problem's folder: P22 and P42 read their data file from the current directory.

**C++**

```
cd P6
g++ -O2 -o P6 P6.cpp
echo 100 | ./P6
```

The C++ programs read their input from standard input; each folder's `README.md` gives the exact command. Compiled binaries are git-ignored, so only the `.cpp` source is tracked.
