import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    res = df[df[column] > threshold]
    return {
        "filtered_data" : res.to_dict('list'),
        "count" : res.shape[0]
    }
    
    