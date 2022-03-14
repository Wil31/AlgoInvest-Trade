import time
from itertools import combinations
from unittest import result
from tools import calculate_spent
from config import ACTIONS, DATASET1, BUDGET

def dynamic_algo(data, max_spending):

    max_spending *= 100

    # Get the number of actions
    n = len(data)

    # Create a matrix with n rows and max_spending number of columns
    matrix = [[0] * (max_spending + 1) for i in range(n)]
    
    # Sort actions per costs
    data.sort(key=lambda x: x[1])

    # Get a list of profit for every action in data
    profits = [a[1] * a[2] for a in data]

    # Convert cost of action in points to get only integers
    weights = [int(a[1] * 100) for a in data]

    for p in range(weights[0], max_spending + 1):
        # 
        matrix[0][p] = profits[0]
    for i in range(1, n):
        for p in range(weights[i]):
            matrix[i][p] = matrix[i - 1][p]
        for p in range(weights[i], max_spending + 1):
            matrix[i][p] = max(matrix[i - 1][p], profits[i] + matrix[i - 1][p - weights[i]])

    # return matrix[-1][-1]


    # Find the selected shares from the matrix
    w = max_spending
    n = len(data)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = data[n-1]
        if matrix[n][w] == matrix[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrix[-1][-1], elements_selection

def main():
    # Initiate chronometer
    start = time.time()

    result = dynamic_algo(ACTIONS, BUDGET)
    # print(result)
    print(f"--- Dynamic algo (DATASET1) ---\n \
    Total costs : {calculate_spent(result[1])}\n \
    Maximum total profit : {result[0]}\n \
    Selected actions: {result[1]}")

    # Calculate runtime and display
    end = time.time()
    delta_time = end - start
    print(f"\n ## The program runs in {delta_time} seconds ##\n")


main()
