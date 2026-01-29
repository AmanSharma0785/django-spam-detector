# Spam Detection System – Data Analytics & Machine Learning Project

This project is an end-to-end **Data Analytics + Machine Learning application** that analyzes text data and classifies messages or emails as **Spam** or **Not Spam**.  
It demonstrates how data preprocessing, feature engineering, and statistical modeling are used to solve a real-world classification problem.

---

## Project Objective

The objective of this project is to:
- Analyze text data using data analytics techniques
- Convert unstructured text into numerical features
- Build a predictive classification model
- Deploy the analytical model through a web interface

This project reflects a **Data Analyst’s workflow**, from raw data to actionable insights.

---

## Problem Statement

Spam messages are a common issue in emails and messaging platforms.  
The challenge is to **analyze textual patterns** and **identify spam messages accurately** using data-driven techniques.

---

## Data Analytics Workflow

1. **Data Understanding**
   - Labeled dataset containing spam and non-spam messages
   - Binary target variable (Spam = 1, Not Spam = 0)

2. **Data Preprocessing**
   - Text normalization (lowercasing)
   - Removal of noise and irrelevant tokens
   - Preparation of clean analytical features

3. **Feature Engineering**
   - Conversion of text data into numerical format
   - Bag-of-Words representation using CountVectorizer

4. **Model Building**
   - Statistical classification using Multinomial Naive Bayes
   - Suitable for frequency-based text features

5. **Model Evaluation**
   - Train-test split
   - Accuracy and prediction validation

6. **Model Deployment**
   - Saving trained model using Joblib
   - Loading model for real-time prediction via Django

---

## Key Features

-  Text data analysis and feature extraction
-  Statistical machine learning model
-  Spam prediction based on learned data patterns
-  Model persistence using Joblib
-  Interactive interface to test analytical results
-  Reusable analytics pipeline

---

## Tools & Technologies

- **Programming Language:** Python  
- **Data Analysis & ML:**  
  - Pandas  
  - NumPy
  - Matplotlib
  - Scikit-learn  
- **Text Analytics:** CountVectorizer  
- **Model:** Multinomial Naive Bayes  
- **Model Serialization:** Joblib  
- **Backend (Deployment):** Django  
- **Version Control:** Git & GitHub  

---

## Project Structure

mldeploy/
│
├── home/
│   ├── views.py          # Prediction logic
│   ├── utils.py          # Text preprocessing
│   ├── urls.py
│   ├── templates/
│   │   └── index.html    # UI for testing predictions
│   ├── savedModels/
│   │   ├── spam_model.joblib
│   │   └── vectorizer.joblib
│
├── manage.py
├── requirements.txt
└── README.md


---

## How to Run the Project

```bash
git clone https://github.com/YOUR_USERNAME/django-spam-detector.git
cd django-spam-detector
pip install -r requirements.txt
python manage.py runserver
```

---

## Open in browser:
http://127.0.0.1:8000/

---

## Sample Analysis Inputs

1. **Spam Message**
   - Congratulations! You have won ₹5,00,000. Click now to claim.
 
2. **Not Spam Message**
   - Please review the sales report and share your feedback.






