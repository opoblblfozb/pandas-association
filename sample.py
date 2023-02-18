import pandas as pd
import pandas_association

from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "tests" / "resources" / "sampledata.csv")
association = pandas_association.Association(df)

cramer_ranking = association.make_contribution_ranking("col1", ["col2", "col3"], method="cramer")