import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)
    element = df.iat[row, col]
    row_values = df.iloc[row].tolist()
    col_values = df.iloc[:, col].tolist()
    return [ element, row_values, col_values ]