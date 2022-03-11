import time
from itertools import combinations
from tools import calculate_gain, calculate_spent
from config import ACTIONS, DATASET1, DATASET2, BUDGET


def bruteforce(data, max_spending):
    """
    Brute force algorithm which tries all combinations of actions
    """
    max_profit = [-1, []]
    for i in range(1, len(data)):
        combination = combinations(data, i)
        for wallet in combination:
            if calculate_spent(wallet) <= max_spending:
                gain = calculate_gain(wallet)
                if gain > max_profit[0]:
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
