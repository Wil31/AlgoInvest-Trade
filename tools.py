def calculate_spent(actions):
    """
    Returns the total spent for a list of actions
    """
    spent = 0
    for i in range(len(actions)):
        spent += actions[i][1]
    return spent


def calculate_gain(actions):
    """
    Calculate the total gain for a list of actions
    """
    gain = 0
    for i in range(len(actions)):
        gain += actions[i][1] * actions[i][2]
    return gain