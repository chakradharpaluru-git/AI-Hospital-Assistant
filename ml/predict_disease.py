import os
import joblib
import pandas as pd


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "disease_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "disease_encoder.pkl"
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "disease_dataset.csv"
)


# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(DATASET_PATH)

df = df.loc[
    :,
    ~df.columns.str.contains("^Unnamed")
]

feature_names = list(
    df.drop(
        "prognosis",
        axis=1
    ).columns
)


# ==========================================================
# MODEL CACHE
# ==========================================================

_model = None
_encoder = None


# ==========================================================
# LOAD MODEL ONLY WHEN NEEDED
# ==========================================================

def get_model():

    global _model

    if _model is None:

        print("Loading disease prediction model...")

        _model = joblib.load(
            MODEL_PATH
        )

        print("Disease prediction model loaded.")

    return _model


# ==========================================================
# LOAD ENCODER ONLY WHEN NEEDED
# ==========================================================

def get_encoder():

    global _encoder

    if _encoder is None:

        print("Loading disease encoder...")

        _encoder = joblib.load(
            ENCODER_PATH
        )

        print("Disease encoder loaded.")

    return _encoder


# ==========================================================
# DISEASE PREDICTION
# ==========================================================

def predict(
    selected_symptoms: list[str]
):

    # Load only when prediction endpoint is used
    model = get_model()

    encoder = get_encoder()


    # ------------------------------------------------------
    # Create symptom vector
    # ------------------------------------------------------

    symptom_vector = [
        0
    ] * len(feature_names)


    for symptom in selected_symptoms:

        symptom = (
            symptom
            .strip()
            .lower()
        )


        if symptom in feature_names:

            index = feature_names.index(
                symptom
            )

            symptom_vector[index] = 1


    # ------------------------------------------------------
    # Create DataFrame
    # ------------------------------------------------------

    data = pd.DataFrame(
        [symptom_vector],
        columns=feature_names
    )


    # ------------------------------------------------------
    # Debug information
    # ------------------------------------------------------

    print("=" * 60)

    print(
        "Selected Symptoms:",
        selected_symptoms
    )

    print(
        "Matched Symptoms :",
        data.columns[
            data.iloc[0] == 1
        ].tolist()
    )


    # ------------------------------------------------------
    # Prediction
    # ------------------------------------------------------

    prediction = model.predict(
        data
    )

    probabilities = model.predict_proba(
        data
    )


    # ------------------------------------------------------
    # Decode disease
    # ------------------------------------------------------

    disease = encoder.inverse_transform(
        prediction
    )[0]


    # ------------------------------------------------------
    # Confidence
    # ------------------------------------------------------

    confidence = round(
        probabilities.max() * 100,
        2
    )


    # ------------------------------------------------------
    # Debug information
    # ------------------------------------------------------

    print(
        "Prediction Index :",
        prediction
    )

    print(
        "Disease          :",
        disease
    )

    print(
        "Confidence       :",
        confidence
    )

    print("=" * 60)


    # ------------------------------------------------------
    # Response
    # ------------------------------------------------------

    return {

        "disease": disease,

        "confidence": confidence

    }