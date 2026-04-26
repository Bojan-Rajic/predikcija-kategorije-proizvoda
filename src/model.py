import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. učitavanje podataka
df = pd.read_csv("data/products.csv")
df.columns = df.columns.str.strip()

# 2. čišćenje
df = df.dropna(subset=["Product Title", "Category Label"])

# 3. normalizacija labela
df["Category Label"] = (
    df["Category Label"]
    .astype(str)
    .str.lower()
    .str.strip()
)

df["Category Label"] = df["Category Label"].replace({
    "mobile phone": "mobile phones",
    "cpu": "cpus",
    "fridge": "fridges"
})

# 4. input i output
X = df["Product Title"]
y = df["Category Label"]

# 5. MODEL PIPELINE
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        lowercase=True
    )),
    ("classifier", LogisticRegression(max_iter=2000))
])

# 6. trening
model.fit(X, y)

# 7. čuvanje modela
joblib.dump(model, "models/model.pkl")

print("Model treniran i sačuvan")