import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================
# Paths
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "disease_dataset.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

os.makedirs(MODEL_DIR, exist_ok=True)

# ==========================
# Load Dataset
# ==========================

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

# Remove empty unnamed columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print("Dataset Shape:", df.shape)

# ==========================
# Features & Target
# ==========================

X = df.drop("prognosis", axis=1)

y = df["prognosis"]

print("Number of Features:", X.shape[1])

# ==========================
# Encode Labels
# ==========================

encoder = LabelEncoder()

y = encoder.fit_transform(y)

# ==========================
# Train/Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================
# Model
# ==========================

print("Training Model...")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Evaluation
# ==========================

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("\nAccuracy :", accuracy)

print("\nClassification Report\n")

print(classification_report(y_test, pred))

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, pred))

# ==========================
# Save Model
# ==========================

joblib.dump(
    model,
    os.path.join(
        MODEL_DIR,
        "disease_model.pkl"
    )
)

joblib.dump(
    encoder,
    os.path.join(
        MODEL_DIR,
        "disease_encoder.pkl"
    )
)

print("\nModel Saved Successfully")