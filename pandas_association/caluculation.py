import pandas as pd
import numpy as np

from scipy.stats.contingency import association
from scipy.stats import entropy

    
def cramer(df:pd.DataFrame, col1:str, col2:str):
    return association(make_cross_matrix(df, col1, col2), method="cramer")
    
def tschuprow(df:pd.DataFrame, col1:str, col2:str):
    return association(make_cross_matrix(df, col1, col2), method="tschuprow")

def pearson(df:pd.DataFrame, col1:str, col2:str):
    return association(make_cross_matrix(df, col1, col2), method="pearson")

def uncertainty_coefficient(df:pd.DataFrame, col1:str, col2:str):
    col1_seq, col2_seq = make_mapped_sequence(df, col1, col2)
    col1_entropy = entropy(col1_seq)
    col1_entropy_conditioned = conditional_entropy(col1_seq, col2_seq)
    return (col1_entropy - col1_entropy_conditioned) / col1_entropy

def make_cross_matrix(df:pd.DataFrame, col1:str, col2:str):
    return np.array(pd.crosstab(df[col1], df[col2]).values, dtype=np.int64)

def make_mapped_sequence(df:pd.DataFrame, col1:str, col2:str):
    col1_mapping = {v:i for i, v in enumerate(df[col1].unique())}
    col2_mapping = {v:i for i, v in enumerate(df[col2].unique())}
    return np.array(df[col1].map(col1_mapping).values, dtype=np.int64), np.array(df[col2].map(col2_mapping), dtype=np.int64)

def conditional_entropy(target_sequence: np.ndarray, condition_sequence:np.ndarray):
    n = len(target_sequence)
    res = 0
    for condition in set(condition_sequence):
        distribution = target_sequence[condition_sequence == condition]
        probs = len(distribution) / n
        res += probs * entropy(distribution)
    return res