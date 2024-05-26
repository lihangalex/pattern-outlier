import pandas as pd

def load_transaction_data(file_path):
    return pd.read_csv(file_path)

def binarize_data(df):
    return (df > 0).astype(int)
