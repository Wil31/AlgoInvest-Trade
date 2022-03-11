import csv


def convert_csv_to_list(fichier: str) -> list:
    """
    Returns a list of actions from a CSV file
    """
    with open(fichier, newline='') as datafile:
        actions = list(csv.reader(datafile, delimiter=',', quotechar='|'))[1:]
    actions = [[a[0], float(a[1]), float(a[2][:-1])/100]
               for a in actions if float(a[1]) >= 0]
    return actions


BUDGET = 500
FILES = ['data/actions.csv', 'data/dataset1.csv', 'data/dataset2.csv']
ACTIONS = convert_csv_to_list(FILES[0])
DATASET1 = convert_csv_to_list(FILES[1])
DATASET2 = convert_csv_to_list(FILES[2])
