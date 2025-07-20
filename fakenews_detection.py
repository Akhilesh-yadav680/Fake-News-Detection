!pip install pandas numpy scikit-learn gradio joblib
import pandas as pd

# Download dataset if needed, or upload manually
df_fake = pd.read_csv("/content/fake_news_dataset/Fake.csv")
df_true = pd.read_csv("/content/fake_news_dataset/True.csv")

df_fake['label'] = 0  # Fake
df_true['label'] = 1  # Real

df = pd.concat([df_fake, df_true])[['text', 'label']]
df = df.sample(frac=1).reset_index(drop=True)  # Shuffle
df.head()
import zipfile
import os

# Define file paths
zip_path = "/content/fake.zip"
extract_to = "/content/fake_news_dataset"

# Create directory and extract
os.makedirs(extract_to, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("✅ Extraction complete!")
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Save
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Accuracy:", accuracy_score(y_test, model.predict(X_test_vec)))
import gradio as gr
import joblib
import numpy as np  # make sure numpy is explicitly imported too

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Define prediction function
def predict_news(news_text):
    vec = vectorizer.transform([news_text])
    pred = model.predict(vec)[0]
    return "✅ Real News" if pred == 1 else "❌ Fake News"

# Gradio UI
iface = gr.Interface(
    fn=predict_news,
    inputs=gr.Textbox(lines=10, placeholder="Paste a news article here..."),
    outputs="text",
    title="📰 Fake News Detector",
    description="Enter news text to detect if it's Real or Fake.",
)

iface.launch(share=True)
