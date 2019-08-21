### [Oversized Pancake Flipper](https://code.google.com/codejam/contest/3264486/dashboard#s=p0)

### Solution

The problem is rather simple and can be solved with the following steps:

1. Check if all the pancakes are happy-faced. If not, find the first sad-faced pancake from the right.
2. From that location inclusive, flip `n` pancakes on the left side.
3. Keep repeating till no flips are possible or we get all happy faced pancakes.