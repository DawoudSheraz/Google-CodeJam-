### [Saving The Universe](https://code.google.com/codejam/contest/32013/dashboard) 

### Solution

For the solution, the challenge is to find the optimal engine for every case. That could range from choosing the engine with minimum hits or not hits. The proposed solution is as follows:

1. From the given data, construct 2 different dictionaries. One will contain the number of hits for each engine and one will comprise of list of indices, where the engine will be hit in the query, for each engine.
2. After creating the dictionary, the next step is to choose the optimal engine. The optimal engine from a given set of data will be:
   - The minimum hit index when each engine will be hit. The minimum specifies the first hit point for an engine.
   - Among all the minimum index, choose the engine that will be hit at the last i.e. the max value from the list of the minimum indices.
3. When optimal engine is selected, loop the query list until the currently selected optimal engine comes up in the query. Here, the switch would happen.
4. The switch will require choosing a next optimal engine. The additional condition for choosing the new optimal engine is that currently selected engine is not to be selected(as it is to be switched).
5. Update the dictionaries with the latest data.