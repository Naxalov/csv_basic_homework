def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """

    row = data.split('\n')
    return len(row[0].split(','))

# Read the csv file
data = open('data.csv').read()
print(find_number_of_columns(data))