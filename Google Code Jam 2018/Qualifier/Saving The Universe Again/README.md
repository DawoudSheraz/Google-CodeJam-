### [Saving the Universe Again](https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007966)

### Solution

To be able to sustain the damage uptil the defense, it is necessary to delay the robot's charge instruction as much as possible. This means the possible swap is to change CS statement into SC. If fire is already shot, the charge will have no effect. The algorithm is as:

1. Calculate damage of the original instruction. If less than or equal to defense, don't move ahead.
2. If 1 is not true, find the rightmost CS pattern.
3. If found, swap, increase swap count and calculate new damage.
4. If damage still higher than defense, repeat 2-3.
5. If no more pattern exists, calculate damage and:
    - if it is less than or equal to defense, return total swaps
    - If greater than defense, return IMPOSSIBLE