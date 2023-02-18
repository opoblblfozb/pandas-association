import pandas as pd
from typing import Iterable
from pandas_association.caluculation import cramer, tschuprow

class Association:
    def __init__(self, df: pd.DataFrame):
        self.data_table = df
        
    def caluculate(self, col1:str, col2:str, method:str):
        if method=="tschuprow":
            return  tschuprow(self.data_table, col1, col2)
        elif method=="cramer":
            return cramer(self.data_table, col1, col2)
        else:
            raise NotImplementedError(f"method: {method} is not impremented")
        
    def make_contribution_ranking(self, target_colname:str, explain_colnames:Iterable[str], method:str):
        values = []
        for e in explain_colnames:
            values.append(self.caluculate(target_colname, e, method=method))
        return pd.DataFrame({method: values}, index=explain_colnames).sort_values(by=method, ascending=False)