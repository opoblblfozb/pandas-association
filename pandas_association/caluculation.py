import pandas as pd
import numpy as np

from scipy.stats.contingency import association

def make_cross_matrix(df:pd.DataFrame, col1:str, col2:str):
    return np.array(pd.crosstab(df[col1], df[col2]).values, dtype=np.int64)

def cramer(df:pd.DataFrame, col1:str, col2:str):
    matrix = make_cross_matrix(df, col1, col2)
    return association(matrix, method="cramer")
    
def tschuprow(df:pd.DataFrame, col1:str, col2:str):
    ...