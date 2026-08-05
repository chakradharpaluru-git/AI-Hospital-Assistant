import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "disease_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "disease_encoder.pkl")
DATASET_PATH = os.path.join(BASE_DIR, "datasets", "disease_dataset.csv")

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

df = pd.read_csv(DATASET_PATH)
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

feature_names = list(df.drop("prognosis", axis=1).columns)


def predict(selected_symptoms: list[str]):

    symptom_vector = [0] * len(feature_names)

    for symptom in selected_symptoms:

        symptom = symptom.strip().lower()

        if symptom in feature_names:
            index = feature_names.index(symptom)
            symptom_vector[index] = 1

    data = pd.DataFrame(
        [symptom_vector],
        columns=feature_names
    )

    print("=" * 60)
    print("Selected Symptoms:", selected_symptoms)
    print("Matched Symptoms :", data.columns[data.iloc[0] == 1].tolist())

    prediction = model.predict(data)
    probabilities = model.predict_proba(data)

    disease = encoder.inverse_transform(prediction)[0]

    confidence = round(probabilities.max() * 100, 2)

    print("Prediction Index :", prediction)
    print("Disease          :", disease)
    print("Confidence       :", confidence)
    print("=" * 60)

    return {
        "disease": disease,
        "confidence": confidence
    }