### [Vestigium](https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c)

### Solution

This problem had a pretty straight forward solution. Trace is self-explanatory. For the rest:

- To find the repeating elements in the row, convert the list into set and if the original list and new set lengths aren't equal, there are repeating elements in that row
- For repitition in the column, take the transpose of the matrix and apply the row check(which is column check due to matrix being transposed)
