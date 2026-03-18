import numpy as np

def matrix_transpose(A):
    rows = len(A)
    cols = len(A[0])

    result = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j]
            
    return result