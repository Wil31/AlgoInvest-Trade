import time


def greedy(data, max_spendings):
    """
    Greedy algorithm that chooses the best solution available at the time.
    It isn't concerned about wether the current best outcome 
    will provide the best overall result.
    It is a top down approach.
    Time complexity: O(NlogN) because of the sorting required.
    Space complexity: O(1) because no additional memory required
    """
    actions_selected = []
    spendings = 0
    earnings = 0

    # Sort the list of actions per highest rate first
    actions_sorted = sorted(data, key=lambda x: x[2], reverse=True)

    # For every action in the sorted list:
    for action in actions_sorted:
        # check total spendings have not reached max spending cap
        if spendings == max_spendings:
            break
        # check next action will not go over the max spending cap
        elif (spendings + action[1]) <= max_spendings:
            spendings += action[1]
            earnings += action[1] * action[2] / 100
            actions_selected.append(action)

    # Show results:
    print(f"Total spendings : {spendings}")
    print(f"Total earnings : {earnings}")
    print("Actions selected :")
    for action in actions_selected:
        print(action[0])


def main():
    # Initiate chronometer
    start = time.time()

    # List of given actions [name, price, percentage]
    actions = [
        ["action_01", 20, 5],
        ["action_02", 30, 10],
        ["action_03", 50, 15],
        ["action_04", 70, 20],
        ["action_05", 60, 17],
        ["action_06", 80, 25],
        ["action_07", 22, 7],
        ["action_08", 26, 11],
        ["action_09", 48, 13],
        ["action_10", 34, 27],
        ["action_11", 42, 17],
        ["action_12", 110, 9],
        ["action_13", 38, 23],
        ["action_14", 14, 1],
        ["action_15", 18, 3],
        ["action_16", 8, 8],
        ["action_17", 4, 12],
        ["action_18", 10, 14],
        ["action_19", 24, 21],
        ["action_20", 114, 18],
    ]
    max_spending = 500

    greedy(actions, max_spending)

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
