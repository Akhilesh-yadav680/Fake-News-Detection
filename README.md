
# 📰 Fake News Detection System

This project is a **Fake News Detection Web App** built using **Scikit-learn** and **Gradio**. It uses a machine learning model trained on news data to classify whether a given news article is **Real** or **Fake**.

## 🚀 Features

- Predicts whether a news article is Real or Fake.
- Simple and interactive Gradio web interface.
- Model built using `TfidfVectorizer` and a trained classifier (saved as `.pkl` files).

---

## 📂 Project Structure

```
fake-news-project/
│
├── app.py                 # Gradio frontend code        
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)
```
## 📂 Dataset

This project uses the [Fake News Detection dataset from Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset).  
Please download the `Fake.csv` and `True.csv` files manually or via Kaggle API.

---

## 🛠️ Installation

### 1.Download Dataset 


### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python app.py
```

You will get a local and a public **Gradio link**. Open it in your browser to test the app.

---

## 📸 Example

> **Input:**
> > "Breaking: Prime Minister announces new AI initiative to improve healthcare."

> **Output:**
> > ✅ Real News

---

## 📦 Dependencies

- Python 3.10
- numpy 1.24.3
- pandas
- scikit-learn
- joblib
- gradio

You can install all using:

```bash
pip install -r requirements.txt
```

---

## 📬 Contact

Made  by **Akhilesh**

Feel free to connect on [GitHub](https://github.com/your-username) or raise an issue if you have questions!

---
