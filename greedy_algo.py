import time
from config import ACTIONS, DATASET1, DATASET2, BUDGET


def greedy(data, max_spendings):
    """
    Greedy algorithm that chooses the best solution available at the time,
    and returns the max profit, total cost and list of selected actions.
    It isn't concerned about wether the current best outcome will provide 
    the best overall result. It is a top down approach.
    Time complexity: O(NlogN) because of the sorting required.
    Space complexity: O(N) no additional memory required
    """
    actions_selected = []
    spendings = 0
    earnings = 0

    # Sort the list of actions per highest rate first
    actions_sorted = sorted(data, key=lambda x: x[2], reverse=True)

    # For every action in the sorted list:
    for action in actions_sorted:
        # Check if total spendings has not reached threshold
        if spendings == max_spendings:
            break
        # Check next action will not go over threshold
        elif (spendings + action[1]) <= max_spendings:
            spendings += action[1]
            earnings += action[1] * action[2]
            actions_selected.append(action)

    return spendings, earnings, actions_selected


def main():
    # Initiate chronometer
    start = time.time()

    result = greedy(ACTIONS, BUDGET)
    print(f"--- Greedy algorithm (20 actions) ---\n \
    Total costs : {result[0]}\n \
    Maximum total profit : {result[1]}\n \
    Selected actions: {result[2]}")

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")

    start = time.time()

    result2 = greedy(DATASET1, BUDGET)
    print(f"--- Greedy algorithm (DATASET1) ---\n \
    Total costs : {result2[0]}\n \
    Maximum total profit : {result2[1]}\n \
    Selected actions: {result2[2]}")

    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")

    start = time.time()

    result3 = greedy(DATASET2, BUDGET)
    print(f"--- Greedy algorithm (DATASET2) ---\n \
    Total costs : {result3[0]}\n \
    Maximum total profit : {result3[1]}\n \
    Selected actions: {result3[2]}")

    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
