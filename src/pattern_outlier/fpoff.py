from mlxtend.frequent_patterns import apriori

class FPOF:
    def __init__(self, min_support=0.5):
        self.min_support = min_support
        self.frequent_itemsets = None

    def fit(self, df):
        self.frequent_itemsets = apriori(df, min_support=self.min_support, use_colnames=True)
        return self

    def score(self, df):
        scores = []
        for index, transaction in df.iterrows():
            score = 0
            for itemset in self.frequent_itemsets['itemsets']:
                if not itemset.issubset(set(transaction[transaction == 1].index)):
                    score += 1
            scores.append(score)
        return scores

    def predict(self, df, threshold):
        scores = self.score(df)
        return [1 if score > threshold else 0 for score in scores]
