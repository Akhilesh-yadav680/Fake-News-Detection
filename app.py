import gradio as gr
import joblib
import numpy as np

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

if __name__ == "__main__":
    iface.launch()
