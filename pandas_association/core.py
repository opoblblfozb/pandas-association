import pandas as pd
import numpy as np

from typing import Iterable, Sequence
from pandas_association.caluculation import cramer, tschuprow, pearson, uncertainty_coefficient


class Association:
    def __init__(self, df: pd.DataFrame):
        self.data_table = df
        self.association_methods = {
            "tschuprow": tschuprow,
            "cramer": cramer,
            "pearson": pearson,
            "uncertainty_coefficient": uncertainty_coefficient
        }
        
    def caluculate(self, col1:str, col2:str, method:str) -> float:
        association_method = self.association_methods.get(method)
        if association_method:
            return self.association_methods.get(method)(self.data_table, col1, col2)
        else:
            raise NotImplementedError(f"method {method} is not implemented")
    
    def make_contribution_ranking(self, target_colname:str, explain_colnames:Iterable[str], method:str):
        values = []
        for e in explain_colnames:
            values.append(self.caluculate(target_colname, e, method=method))
        return pd.DataFrame({method: values}, index=explain_colnames).sort_values(by=method, ascending=False)
    
    def make_all_contibution_ranking(self, target_colname:str, explain_colnames:Iterable[str]):
        results  = []
        for method_name in self.association_methods.keys():
            results.append(self.make_contribution_ranking(target_colname, explain_colnames, method_name))
        return pd.concat(results, axis=1)

    def make_association_map(self, columns:Sequence[str], method="cramer"):
        matrix = np.zeros((len(columns), len(columns))) 
        for i, col1 in enumerate(columns):
            for j, col2 in enumerate(columns):
                matrix[i, j] = self.caluculate(col1, col2, method=method)
        return pd.DataFrame(matrix, index=columns, columns=columns)
        