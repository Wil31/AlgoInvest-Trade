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


def sort_best_actions(data, max_spendings):
    actions_selected = []
    spendings = 0
    earnings = 0

    # Calculate gain for every action and add the data to the list
    for action in data:
        gain = action[1] * action[2] / 100
        action.append(gain)

    # Sort the list of actions per highest rate first
    actions_sorted = sorted(data, key=lambda x: x[2], reverse=True)

    # For every action in the sorted list:
    # check total spendings have not reached spending cap: if yes stop the loop;
    # check next action will not go over the max spending cap: if yes ignore it;
    # else: retain this action.
    for action in actions_sorted:
        if spendings == max_spendings:
            break
        elif (spendings + action[1]) > max_spendings:
            continue
        else:
            spendings += action[1]
            earnings += action[3]
            actions_selected.append(action)

    # Show results:
    print(f"Total spendings : {spendings}")
    print(f"Total earnings : {earnings}")
    print("Actions selected :")
    for action in actions_selected:
        print(action)


sort_best_actions(actions, 500)
