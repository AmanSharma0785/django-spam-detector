import streamlit as st
import joblib
import os

# page config
st.set_page_config(page_title="Spam Detector", page_icon="🚨")

# load model & vectorizer
BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(
    BASE_DIR, "home", "savedModels", "spam_model.joblib"
))

vectorizer = joblib.load(os.path.join(
    BASE_DIR, "home", "savedModels", "vectorizer.joblib"
))

# preprocessing (same as Django utils)
def transform_text(text):
    text = text.lower()
    return text

# UI
st.title("🚨 Spam Message Detector")
st.write("Enter a message or email to check whether it is spam or not.")

user_input = st.text_area("Message", height=150)

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        processed = transform_text(user_input)
        vector = vectorizer.transform([processed])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚨 SPAM MESSAGE")
        else:
            st.success("✅ NOT SPAM")
