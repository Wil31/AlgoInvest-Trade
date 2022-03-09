import time


def bruteforce(max_spending, data, selected_actions=[]):
    """
    Brute force algorithm which tries all possible solutions
    """
    if data:
        # val1 and lst_val1 are the results of bruteforce (max earnings, selected actions),
        # without current action
        val1, lst_val1 = bruteforce(max_spending, data[1:], selected_actions)

        # Select an action in the list
        action = data[0]

        if action[1] <= max_spending:
            # We use bruteforce while subtracting the amount of current action from max_spending,
            # we add this action to selected_actions
            val2, lst_val2 = bruteforce(max_spending - action[1], data[1:],
                                        selected_actions + [action])

            # We test the best profitability between the 2 solutions
            if val1 < val2:
                return val2, lst_val2
        return val1, lst_val1

    else:
        # Return at last the total profitability,
        # and the list of selected actions and the max amount spent
        return f"Maximum profitability : \
            {round(sum([i[1] * i[2] for i in selected_actions]), 2)}", \
            f"Maximum spent : {sum([i[1] for i in selected_actions])}, " \
            f"Selected actions : {[i[0] for i in selected_actions]}"


def main():
    # Initiate chronometer
    start = time.time()

    actions = [
        ["action_01", 20, 0.05],
        ["action_02", 30, 0.1],
        ["action_03", 50, 0.15],
        ["action_04", 70, 0.2],
        ["action_05", 60, 0.17],
        ["action_06", 80, 0.25],
        ["action_07", 22, 0.07],
        ["action_08", 26, 0.11],
        ["action_09", 48, 0.13],
        ["action_10", 34, 0.27],
        ["action_11", 42, 0.17],
        ["action_12", 110, 0.09],
        ["action_13", 38, 0.23],
        ["action_14", 14, 0.01],
        ["action_15", 18, 0.03],
        ["action_16", 8, 0.08],
        ["action_17", 4, 0.12],
        ["action_18", 10, 0.14],
        ["action_19", 24, 0.21],
        ["action_20", 114, 0.18],
    ]
    max_spending = 500

    print(bruteforce(max_spending, actions))

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
