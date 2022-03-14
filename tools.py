import csv


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


def convert_csv_to_list(fichier: str) -> list:
    """
    Returns a list of actions from a CSV file
    """
    with open(fichier, newline='') as datafile:
        actions = list(csv.reader(datafile, delimiter=',', quotechar='|'))[1:]
    actions = [[a[0], float(a[1]), float(a[2][:-1])/100]
               for a in actions if float(a[1]) > 0]
    return actions
