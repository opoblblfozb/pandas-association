from unittest import TestCase
from unittest.mock import MagicMock, patch, call

import pandas as pd
from pandas.testing import assert_frame_equal

from pandas_association import Association

class AssociationTestCase(TestCase):
    def test__init(self):
        df = MagicMock(spec=pd.DataFrame)
        
        sut = Association(df)
        
        self.assertEqual(sut.data_table, df)
    
    @patch("pandas_association.core.Association.caluculate")    
    def test_make_contribution_ranking(self, calculate):
        sut = Association(MagicMock(spec=pd.DataFrame))
        target_colname = "target_colname"
        explain_colnames = ["explain_colname1", "explain_colname2"]
        calculate.side_effect = [0.3, 0.4]
        
        actual = sut.make_contribution_ranking(target_colname=target_colname, explain_colnames=explain_colnames, method="cramer")

        calculate.assert_has_calls([call("target_colname", "explain_colname1", method="cramer"),
                                    call("target_colname", "explain_colname2", method="cramer")])
        assert_frame_equal(actual, pd.DataFrame({"cramer": [0.4, 0.3]}, index=["explain_colname2", "explain_colname1"]))
    
    @patch("pandas_association.core.cramer")    
    def test_caluculate_cramer(self, cramer):
        df = MagicMock(spec=pd.DataFrame)
        
        sut = Association(df)
        actual = sut.caluculate("col1_name", "col2_name", method="cramer")
        
        self.assertEqual(actual, cramer.return_value)

    @patch("pandas_association.core.tschuprow")    
    def test_caluculate_tchuprow(self, tchuprow):
        df = MagicMock(spec=pd.DataFrame)
        
        sut = Association(df)
        actual = sut.caluculate("col1_name", "col2_name", method="tschuprow")
        
        self.assertEqual(actual, tchuprow.return_value)

    @patch("pandas_association.core.pearson")    
    def test_caluculate_person(self, pearson):
        df = MagicMock(spec=pd.DataFrame)
        
        sut = Association(df)
        actual = sut.caluculate("col1_name", "col2_name", method="pearson")
        
        self.assertEqual(actual, pearson.return_value)

    @patch("pandas_association.core.uncertainty_coefficient")    
    def test_caluculate_person(self, uncertainty_coefficient):
        df = MagicMock(spec=pd.DataFrame)
        
        sut = Association(df)
        actual = sut.caluculate("col1_name", "col2_name", method="uncertainty_coefficient")
        
        self.assertEqual(actual, uncertainty_coefficient.return_value)