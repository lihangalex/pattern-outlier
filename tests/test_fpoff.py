import unittest
from src.pattern_outlier.fpoff import PatternOutlierDetector

class TestPatternOutlierDetector(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            ['Bread', 'Milk', 'Diapers'],
            ['Bread', 'Beer', 'Eggs'],
            ['Milk', 'Diapers', 'Beer'],
            ['Bread', 'Milk', 'Diapers', 'Beer'],
            ['Bread', 'Milk', 'Diapers', 'Eggs'],
            ['Milk', 'Beer', 'Eggs'],
            ['Bread', 'Milk'],
            ['Bread', 'Diapers', 'Beer'],
            ['Milk', 'Diapers'],
            ['Bread', 'Beer'],
            ['Milk', 'Eggs'],
            ['Diapers', 'Beer', 'Eggs'],
            ['Bread', 'Milk', 'Diapers', 'Beer', 'Eggs'],
            ['Bread', 'Beer', 'Diapers'],
            ['Milk', 'Diapers', 'Eggs'],
            ['Bread', 'Milk', 'Beer'],
            ['Bread', 'Diapers'],
            ['Milk', 'Beer'],
            ['Bread', 'Eggs'],
            ['Beer', 'Eggs'],
            ['Chocolate', 'Beer'],
            ['Milk', 'Candy'],
            ['Bread', 'Diapers', 'Candy'],
            ['Beer', 'Diapers', 'Candy'],
            ['Bread', 'Milk', 'Eggs', 'Candy']
        ]

    def test_fit_and_score(self):
        detector = PatternOutlierDetector(min_support=0.3, method='FPI')
        detector.fit(self.transactions)
        scores = detector.score(self.transactions)
        self.assertEqual(len(scores), len(self.transactions))

    def test_predict(self):
        detector = PatternOutlierDetector(min_support=0.3, method='FPI')
        detector.fit(self.transactions)
        predictions = detector.predict(self.transactions, threshold=2)
        self.assertEqual(len(predictions), len(self.transactions))

    def test_save_and_load_model(self):
        detector = PatternOutlierDetector(min_support=0.3, method='FPI')
        detector.fit(self.transactions)
        detector.save_model('test_model.pkl')
        loaded_detector = PatternOutlierDetector.load_model('test_model.pkl')
        predictions = loaded_detector.predict(self.transactions, threshold=2)
        self.assertEqual(len(predictions), len(self.transactions))

if __name__ == '__main__':
    unittest.main()
