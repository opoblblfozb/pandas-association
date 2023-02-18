import pandas as pd
import pandas_association

from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "tests" / "resources" / "sampledata.csv")
association = pandas_association.Association(df)

cramer_ranking = association.make_contribution_ranking("col1", ["col3", "col2"], method="cramer")
tschuprow_ranking = association.make_contribution_ranking("col1", ["col3", "col2"], method="tschuprow")
pearson_ranking = association.make_contribution_ranking("col1", ["col3", "col2"], method="pearson")
uncertainty_coefficient_ranking = association.make_contribution_ranking("col1", ["col3", "col2"], method="uncertainty_coefficient")

all_ranking = association.make_all_contibution_ranking("col1", ["col2", "col3"])
association_map = association.make_association_map(["col1", "col2", "col3"])