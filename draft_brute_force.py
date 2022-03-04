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
actions_selected = []
max_spendings = 500
spendings = 0
earnings = 0

for action in actions:
    gain = action[1] * action[2] / 100
    action.append(gain)
    
actions_sorted = sorted(actions, key=lambda x: x[3], reverse=True)

for action in actions_sorted:
    if (spendings + action[1]) > max_spendings:
        continue
    else:
        spendings += action[1]
        earnings += action[3]
        actions_selected.append(action)
         
print("Total spendings :")
print(spendings)
print("Total earnings :")
print(earnings)
print("Actions selected :")
for action in actions_selected:
    print(action)