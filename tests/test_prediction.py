import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from ml.predict_disease import predict

# 132 symptoms
symptoms = [0] * 132

result = predict(symptoms)

print(result)