# AlgoInvest-Trade

## Part 1 - Brute force algorithm

We have a list of 20 shares (data file **actions.csv**), with a given cost and profit rate over 2 years.

The goal is to create an algorithm that maximises the profit after 2 years, for a given amount of budget.

Constraints:
- A share can be bought only once
- A share cannot be fractioned
- Budget is 500€ max

The program must try every possible combination of actions and provide the best result.

See the algorithm in **bruteforce.py**

## Part 2 - Optimisation

In this part we need to explore a much larger set of data (about 1000 shares), the brute force algorithm is no more 
realistic about time and power constraints. This is because of the terrible time complexity of such algorithms 
O(2^N): exponential time, means that every added element in the dataset doubles the runtime.

To enable optimisation, we will not focus anymore on calculating every possible combination.
The constraints stay the same as for Part 1.

I have explored 2 different solutions:
### A greedy algorithm  
See file **greedy_algo.py**  
This algorithm chooses the best solution available at the time, and returns the max profit, 
total cost and list of selected actions.  
It isn't concerned about whether the current best outcome will provide the best overall result.  
It is a top-down approach. We sort the list of shares per best profit at the beginning.  
Where N is the number of actions:
- Time complexity: O(NlogN) because of the sorting needed.
- Space complexity: O(N), uses "1D" lists.

This Algorithm provides a good result in a minimal time, but the result will not always be the best possible.

### A dynamic programming algorithm  
See file **dynamic_algo.py**  
This algorithm uses a 2D matrix to save the best results at every iteration and compares it to the best earlier result.  
Where N is the number of actions:
- Time complexity: O(N*max_spending)
- Space complexity: O(N*max_spending), uses a 2D array.
Further improvements could be made to reduce space complexity, by using a 2D array with only 2 rows or even further with a 
1D array instead of 2D.

This algorithm is more complex but will provide the best possible solution, and the runtime is very diminished because 
we computate only once each sub-problem.  
A less problematic downside of this method could be that auxiliary memory is 
required, in order to store the solution of each sub-problems in a matrix while the program is running.

## Part 3 - Backtesting and optimisation

This part is mainly to compare our results with the given historical results.
