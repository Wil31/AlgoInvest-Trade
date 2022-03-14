import time
from itertools import combinations
from tools import calculate_profit, calculate_spent
from config import ACTIONS, BUDGET


def bruteforce(data, max_spending):
    """
    Brute force algorithm which tries all combinations of actions,
    and return the maximum profit with the list of selected actions.
    Time complexity O(2^N) is exponential time, scalability is terrible.
    Every additional element to the dataset doubles time.
    """
    # Create a list for the maximum profit and the selected actions
    max_profit = [-1, []]

    for i in range(1, len(data)):
        # Iterate through all combinations of i amount of actions
        # Create all the combinations for i amount
        combination = combinations(data, i)
        for wallet in combination:
            # For every wallet in a combination check the total cost is not over the threshold
            if calculate_spent(wallet) <= max_spending:
                # Calculate the profit for actual wallet
                gain = calculate_profit(wallet)
                if gain > max_profit[0]:
                    # If the actual wallet has a better profit than previous, then keep it
                    max_profit[0] = gain
                    max_profit[1] = wallet
    return max_profit


def main():
    # Initiate chronometer
    start = time.time()

    result = bruteforce(ACTIONS, BUDGET)
    print(f"--- Brute force (20 actions) ---\n \
    Total costs : {calculate_spent(result[1])}\n \
    Maximum total profit : {result[0]}\n \
    Selected actions: {result[1]}")

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
