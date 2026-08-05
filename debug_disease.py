import joblib
import pandas as pd

# Load encoder
encoder = joblib.load("models/disease_encoder.pkl")

print("=" * 60)
print("Encoder Classes:")
print(encoder.classes_)
print("=" * 60)

# Load dataset
df = pd.read_csv("datasets/disease_dataset.csv")

print("\nDataset Diseases:\n")
print(df["prognosis"].unique())