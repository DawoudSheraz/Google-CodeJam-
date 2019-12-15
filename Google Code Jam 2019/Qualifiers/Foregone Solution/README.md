### [Foregone Solution](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231)

### Solution

The problem is fairly simple and can be perfomed in O(k) where k in the number of digits in the given number. It goes like:

1. Create an empty list
2. Convert the given integer into a separate list.
3. For each element of list, if the digit is:
    - 4, then subtract 1 from that digit and append 1 to empty list
    - If not 4, append 0 to empty list
4. When the loop is over, convert both lists to integers. They will be the solution