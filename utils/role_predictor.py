import pickle
import pandas as pd

model = pickle.load(
    open("models/model.pkl", "rb")
)

vectorizer = pickle.load(
    open("models/vectorizer.pkl", "rb")
)


def predict_role(text):

    text_vectorized = vectorizer.transform([text])

    prediction = model.predict(text_vectorized)[0]

    probabilities = model.predict_proba(
        text_vectorized
    )[0]

    classes = model.classes_

    results = pd.DataFrame({
        "Role": classes,
        "Confidence": probabilities * 100
    })

    results = results.sort_values(
        by="Confidence",
        ascending=False
    )

    return prediction, results.head(3)