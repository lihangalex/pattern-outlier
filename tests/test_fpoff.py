import unittest
import pandas as pd
from src.pattern_outlier.fpoff import FPOF


class TestFPOF(unittest.TestCase):
    def setUp(self):
        self.data = {'Bread': [1, 1, 0, 1, 0],
                     'Milk': [1, 0, 1, 1, 1],
                     'Diapers': [0, 1, 1, 1, 1],
                     'Beer': [0, 1, 1, 1, 0],
                     'Eggs': [1, 0, 0, 1, 0]}
        self.df = (pd.DataFrame(self.data) > 0).astype(bool)
        self.fpof = FPOF(min_support=0.6)

    def test_fit(self):
        self.fpof.fit(self.df)
        self.assertIsNotNone(self.fpof.frequent_itemsets)

    def test_score(self):
        self.fpof.fit(self.df)
        scores = self.fpof.score(self.df)
        self.assertEqual(len(scores), len(self.df))

    def test_predict(self):
        self.fpof.fit(self.df)
        predictions = self.fpof.predict(self.df, threshold=2)
        self.assertEqual(len(predictions), len(self.df))


if __name__ == '__main__':
    unittest.main()
