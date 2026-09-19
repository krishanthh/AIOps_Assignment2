import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# load dataset
df = pd.read_csv("spam_dataset.csv")

# build pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# train the model
model.fit(df["text"], df["label"])

# save the model
joblib.dump(model, "spam_model.joblib")
