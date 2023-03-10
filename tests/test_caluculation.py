from pandas_association.caluculation import cramer, pearson, uncertainty_coefficient
import pandas as pd

from pathlib import Path
from sklearn import datasets

resource = Path(__file__).parent.resolve() / "resources" / "sampledata.csv"


def test_cramer():
    df = pd.read_csv(resource)
    
    actual1 = cramer(df, "col1", "col2")
    actual2 = cramer(df, "col1", "col3")
    
    assert actual1 > actual2
    
def test_pearson():
    df = pd.read_csv(resource)

    actual1 = pearson(df, "col1", "col2")
    actual2 = pearson(df, "col1", "col3")
    
    assert actual1 > actual2
    
def test_uncertainty_coefficient():
    df = pd.read_csv(resource)

    actual1 = uncertainty_coefficient(df, "col1", "col2")
    actual2 = uncertainty_coefficient(df, "col1", "col3")
    
    assert actual1 > actual2