def calculate_spent(actions):
    """
    Returns the total spent for a list of actions
    """
    spent = 0
    for i in range(len(actions)):
        spent += actions[i][1]
    return spent


def calculate_profit(actions):
    """
    Calculate the total profit for a list of actions
    """
    profit = 0
    for i in range(len(actions)):
        profit += actions[i][1] * actions[i][2]
    return profit