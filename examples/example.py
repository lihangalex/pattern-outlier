from src.pattern_outlier.fpoff import PatternOutlierDetector
from sklearn.metrics import precision_score, recall_score, f1_score

transactions = [
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

# Generate initial labels
def generate_initial_labels(transactions):
    initial_detector = PatternOutlierDetector(min_support=0.3, method='FPI')
    initial_detector.fit(transactions)
    initial_scores = initial_detector.score(transactions)
    threshold = 2
    initial_predictions = [1 if score < threshold else 0 for score in initial_scores]
    return initial_predictions

# Find best parameters based on initial labels
def find_best_parameters(transactions, initial_labels):
    min_support_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    threshold_values = [1, 2, 3, 4, 5]
    methods = ['FPI', 'WFPI', 'FPOF', 'FPCOF']
    best_f1 = 0
    best_params = {}

    for min_support in min_support_values:
        for threshold in threshold_values:
            for method in methods:
                precision, recall, f1 = evaluate_method(transactions, initial_labels, min_support, threshold, method)
                if f1 > best_f1:
                    best_f1 = f1
                    best_params = {'min_support': min_support, 'method': method, 'threshold': threshold}

    return best_params, best_f1

# Evaluate method
def evaluate_method(transactions, labels, min_support, threshold, method):
    detector = PatternOutlierDetector(min_support=min_support, method=method)
    detector.fit(transactions)
    predictions = detector.predict(transactions, threshold)
    precision = precision_score(labels, predictions)
    recall = recall_score(labels, predictions)
    f1 = f1_score(labels, predictions)
    return precision, recall, f1

if __name__ == '__main__':
    initial_labels = generate_initial_labels(transactions)
    best_params, best_f1 = find_best_parameters(transactions, initial_labels)
    print(f"Best Parameters: {best_params}")
    print(f"Best F1 Score: {best_f1}")

    # Fit model with best parameters, excluding threshold
    detector = PatternOutlierDetector(min_support=best_params['min_support'], method=best_params['method'])
    detector.fit(transactions)
    scores = detector.score(transactions)
    predictions = detector.predict(transactions, threshold=best_params['threshold'])

    # Save and load model example
    detector.save_model('pattern_outlier_detector.pkl')
    loaded_detector = PatternOutlierDetector.load_model('pattern_outlier_detector.pkl')
    loaded_predictions = loaded_detector.predict(transactions, threshold=best_params['threshold'])

    print("Loaded Predictions:", loaded_predictions)