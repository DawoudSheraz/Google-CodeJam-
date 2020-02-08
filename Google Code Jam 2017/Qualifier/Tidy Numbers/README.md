### [Tidy Numbers](https://code.google.com/codejam/contest/3264486/dashboard#s=p1)

### Solution

The problem can be solved with the brute force i.e. starting from the given number, if it is not tidy, decrement by 1 until we find the tidy number. However, for a number like 99998, the last tidy number is 89999. This solution will not be viable for very large number. A hint from the above example is showing that if the given number isn't tidy, the last tidy is sure to have a sequence of 9s. The solution is as:

1. Read the number digit by digit.
2. If the next digit isn't larger, decrement the current digit by 1.
3. All remaining digits from that digits onwards are changed to 9.

Take the following examples:

- 123489; which is tidy

- 3454; which isn't tidy. The last tidy will be 3449. The next number is 3450 which isn't tidy either.