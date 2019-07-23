### [Train TimeTable](https://code.google.com/codejam/contest/32013/dashboard#s=p1)

### Solution

Initially, this problem might look tedious, but in actuality, the solution is much simpler. The challenge here is to eliminate all such pairs where departure time > arrival time on a particular station, for both stations. After identifying all such pairs, the number of buses can be found easily. The detailed solution is as:

1. For first station, consider all the departures require buses. This is the initial assumption.
2. For first station, sort the departure times and arrival time in ascending order.
3. For each departure, find the arrival time that is smaller than that departire time. If found, remove both times and recursive call the function with new data.
4. Again, the number of buses is equal to number of departure, but the count has been reduced at the step 3. This will run recursively until no more such pairs exist.
5. When no pairs are left, the remaining departures will be equal to the number of buses required for that station.
6. Repeat steps 1-5 for second station.