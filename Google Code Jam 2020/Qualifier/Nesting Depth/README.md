### [Nesting Depth](https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f)

### Descriptiton

This problem looks challenging but once the idea is figured out, it is relatively easy to code. To approach the problem:

1. For first term in the string, add that number of `(` in the output string, followed by that term/number.
2. After that, if the next number is:
    - Greater than the previous number, add `(` equal to next-previous , followed by current number.
    - Smaller than previous number, add `)` equal to previous-next, followed by current number.
    - If same, only add the number and no bracket.
3. At the end, add `)` equal to the last value to close the balance the brackets.