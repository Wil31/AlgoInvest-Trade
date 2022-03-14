import time


def sort_actions(actions):
    """
    Sort the list of actions per best value
    """
    return sorted(actions, key=lambda x: x[2], reverse=True)


def calculate_spent(actions, selected_actions):
    """
    Returns the total spent for the selected actions
    """
    spent = 0
    for i in range(len(actions)):
        spent += actions[i][1] * selected_actions[i]
    return spent


def calculate_gain(actions, selected_actions):
    """
    Calculate le total gain for the selected actions
    """
    gain = 0
    for i in range(len(actions)):
        gain += selected_actions[i] * (actions[i][1] * actions[i][2] / 100)
    return gain


def recursive_search(actions, max_spending, selected_actions, i):
    """
    Returns the best choice for the given max spending
    """
    if i == len(actions):
        return selected_actions[:]

    # Initiate at an impossible value
    val1 = -1
    if actions[i][1] <= max_spending - calculate_spent(actions, selected_actions):
        selected_actions[i] = 1
        sol1 = recursive_search(actions, max_spending, selected_actions, i + 1)
        val1 = calculate_gain(actions, sol1)

    selected_actions[i] = 0
    sol2 = recursive_search(actions, max_spending, selected_actions, i + 1)
    val2 = calculate_gain(actions, sol2)

    if val1 > val2:
        return sol1[:]
    else:
        return sol2[:]


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

    # Maximum total value to spend
    max_spending = 500

    actions = sort_actions(actions)

    selected_actions = [0 for i in range(len(actions))]

    sol = recursive_search(actions, max_spending, selected_actions, 0)

    package = []  # Reprensents the pack of selected actions
    for i in range(len(actions)):
        if sol[i] == 1:
            package.append(actions[i][0])
    print(f"Best package of actions to choose : {package}")

    total_spent = 0
    for i in range(len(actions)):
        if sol[i] == 1:
            total_spent += actions[i][1]
    print(f"Total spent : {total_spent}")

    total_gain = 0
    for i in range(len(actions)):
        if sol[i] == 1:
            total_gain += actions[i][1] * actions[i][2] / 100
    print(f"Total earned : {round(total_gain, 2)}")

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
