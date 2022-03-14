import time


def solve_knapsack(data, max_spending):
  return knapsack_recursive(data, max_spending, 0)


def knapsack_recursive(data, max_spending, currentIndex, selected_actions=[]):
  # base checks
  if max_spending <= 0 or currentIndex >= len(data):
    return 0

  # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the max_spending, we shouldn't process this
  profit1 = 0
  action = data[0]
  if data[currentIndex][1] <= max_spending:
    profit1 = (data[currentIndex][1] * data[currentIndex][2]) + \
    knapsack_recursive(data, max_spending - data[currentIndex][1], currentIndex + 1, selected_actions + [action])

  # recursive call after excluding the element at the currentIndex
  profit2 = knapsack_recursive(data, max_spending, currentIndex + 1, selected_actions)

  return max(profit1, profit2)


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

    print(solve_knapsack(actions, max_spending))

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
