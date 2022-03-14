from tools import convert_csv_to_list


BUDGET = 500
FILES = ['data/actions.csv', 'data/dataset1.csv', 'data/dataset2.csv']
ACTIONS = convert_csv_to_list(FILES[0])
DATASET1 = convert_csv_to_list(FILES[1])
DATASET2 = convert_csv_to_list(FILES[2])
