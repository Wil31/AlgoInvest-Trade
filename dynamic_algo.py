import time

from config import ACTIONS, BUDGET, DATASET1, DATASET2


def dynamic_algo(data, max_spending):
    """
    Dynamic programming algorithm, that uses a 2D matrix to 
    save the best results at every iteration and compares it to 
    the best previous result.
        ####
    Where N is the number of actions:
    Time complexity: O(N*max_spending)
    Space complexity: O(N*max_spending), uses a 2D array.
    Further improvements could be made to reduce space complexity,
    by using a 2D array with only 2 rows or even further with a
    1D array instead of 2D matrix.
    """

    # Budget and costs are multiplied per 100 in order to work
    # with integers for the matrix.
    max_spending *= 100
    for line in data:
        line[1] = int(line[1] * 100)
        line[2] = line[2] * line[1] / 100  # Calculate the profit per actions

    # Initiate a matrix with the spendings as columns and actions as rows.
    matrix = [[0 for x in range(max_spending + 1)]
              for x in range(len(data) + 1)]

    # Loop on the rows of actions
    for line in range(1, len(data) + 1):
        # Loop on the rows of spendings
        for c in range(1, max_spending + 1):
            # Check if action cost is less than the column spending we are at
            if data[line-1][1] <= c:
                # We add to the matrix the max between the max profit of previous row,
                # and the profit of the current action added to the optimised solution of
                # previous row.

                # Pseudo-code :
                # max(current profit + previous row profit to maximised spending,
                # max profit of previous row)
                matrix[line][c] = max(
                    data[line-1][2] + matrix[line-1][c-data[line-1][1]], matrix[line-1][c])

            # If the spending is higher than budget, we take previous line solution
            else:
                matrix[line][c] = matrix[line-1][c]

    max_profit = matrix[-1][-1] / 100

    # Part 2: get the actions corresponding to the best results
    w = max_spending
    n = len(data)
    actions_selected = []

    # While spendings are >=0 and actions remain
    while w >= 0 and n >= 0:
        # Take the last action, iterate the list backwards
        a = data[n-1]

        # If current profit == current value profit
        #                      - current value profit minus previous spending,
        # then add this action to the list
        if matrix[n][w] == matrix[n-1][w - a[1]] + a[2]:
            actions_selected.append(a)

            # Substract the selected action price from budget
            w -= a[1]

        # Go to next item
        n -= 1

    # Convert back to the initial values
    for line in actions_selected:
        line[1] /= 100
        line[2] = round(line[2] / 100, 3)

    # Calculate the total spent
    spendings = 0

    for a in actions_selected:
        spendings += a[1]

    return max_profit, spendings, actions_selected


def main():
    # Initiate chronometer
    start = time.time()

    result = dynamic_algo(ACTIONS, BUDGET)
    print(f"--- Dynamic algo (20 ACTIONS) ---\n \
    Total costs : {result[1]}\n \
    Maximum total profit : {result[0]}\n \
    Selected actions: {result[2]}")

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")

    start = time.time()

    result = dynamic_algo(DATASET1, BUDGET)
    print(f"--- Dynamic algo (DATASET1) ---\n \
    Total costs : {result[1]}\n \
    Maximum total profit : {result[0]}\n \
    Selected actions: {result[2]}")

    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")

    start = time.time()

    result = dynamic_algo(DATASET2, BUDGET)
    print(f"--- Dynamic algo (DATASET2) ---\n \
    Total costs : {result[1]}\n \
    Maximum total profit : {result[0]}\n \
    Selected actions: {result[2]}")

    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
