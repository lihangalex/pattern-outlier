import pandas as pd
from src.pattern_outlier.fpoff import FPOF

# Create some dummy data
data = {
    'Bread': [1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    'Milk': [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    'Diapers': [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    'Beer': [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    'Eggs': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

# Convert the data to boolean types as recommended
df = df.astype(bool)

# Initialize and fit the FPOF model
fpof = FPOF(min_support=0.3)
fpof.fit(df)

# Score the data
scores = fpof.score(df)
df['outlier_score'] = scores

# Predict outliers
threshold = 2
predictions = fpof.predict(df, threshold)
df['outlier'] = predictions

# Print the results
print("DataFrame with Outlier Scores and Predictions:")
print(df)
