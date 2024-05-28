import pandas as pd
import joblib
from mlxtend.frequent_patterns import apriori

class PatternOutlierDetector:
    def __init__(self, min_support=0.5, method='FPI'):
        self.min_support = min_support
        self.method = method
        self.frequent_itemsets = None

    def _convert_to_matrix(self, transactions):
        all_items = set(item for transaction in transactions for item in transaction)
        encoded_transactions = []

        for transaction in transactions:
            encoded_transaction = {item: (item in transaction) for item in all_items}
            encoded_transactions.append(encoded_transaction)

        return pd.DataFrame(encoded_transactions).astype(bool)

    def fit(self, transactions):
        df = self._convert_to_matrix(transactions)
        self.frequent_itemsets = apriori(df, min_support=self.min_support, use_colnames=True)
        return self

    def score(self, transactions):
        df = self._convert_to_matrix(transactions)
        scores = []
        for index, transaction in df.iterrows():
            score = self._compute_score(transaction)
            scores.append(score)
        return scores

    def _compute_score(self, transaction):
        if self.method == 'FPI':
            return self._fpi_score(transaction)
        elif self.method == 'WFPI':
            return self._wfpi_score(transaction)
        elif self.method == 'FPOF':
            return self._fpof_score(transaction)
        elif self.method == 'FPCOF':
            return self._fpcof_score(transaction)
        else:
            raise ValueError(f"Unknown method: {self.method}")

    def _fpi_score(self, transaction):
        return sum([1 for itemset in self.frequent_itemsets['itemsets'] if itemset.issubset(set(transaction[transaction == 1].index))])

    def _wfpi_score(self, transaction):
        return sum([len(itemset) for itemset in self.frequent_itemsets['itemsets'] if itemset.issubset(set(transaction[transaction == 1].index))])

    def _fpof_score(self, transaction):
        return sum([1 for itemset in self.frequent_itemsets['itemsets'] if itemset.issubset(set(transaction[transaction == 1].index))])

    def _fpcof_score(self, transaction):
        return sum([1 for itemset in self.frequent_itemsets['itemsets'] if not itemset.issubset(set(transaction[transaction == 1].index))])

    def predict(self, transactions, threshold):
        scores = self.score(transactions)
        return [1 if score < threshold else 0 for score in scores]

    def save_model(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def load_model(filepath):
        return joblib.load(filepath)
