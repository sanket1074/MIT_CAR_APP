# 🚗 Car Price Prediction App

A Machine Learning-powered web application that predicts the price of used cars based on various features such as fuel type, mileage, engine capacity, and more.

🔗 **Live App:** https://mitcarapp-vjgynfh3zf3vggpb2rfs2u.streamlit.app/

---

## 📌 Project Overview

Determining the correct price of a used car is a complex task influenced by multiple factors like age, mileage, fuel type, ownership, and engine specifications.

This project provides an **automated solution** using Machine Learning to predict car prices accurately through an interactive web interface built with Streamlit.

---

## 🚀 Features

- 🔹 Predict car price instantly
- 🔹 User-friendly web interface
- 🔹 Real-time ML predictions
- 🔹 Confidence price range (±10%)
- 🔹 Clean and modern UI design
- 🔹 Fully deployed online

---

## 🧠 Machine Learning Model

- Model Used: **Random Forest Regressor**
- Accuracy: **~90% R² Score**
- Evaluation Metric: Mean Absolute Error (~1.09 Lakhs)

---

## 📊 Input Features

- Insurance Validity
- Fuel Type
- Ownership
- Transmission Type
- KMs Driven
- Number of Seats
- Mileage (kmpl)
- Engine Capacity (cc)
- Max Power (bhp)
- Torque (Nm)
- Manufacturing Year

---

## ⚙️ Tech Stack

- **Frontend/UI:** Streamlit
- **Backend:** Python
- **Libraries:**
  - pandas
  - numpy
  - scikit-learn
  - pickle

---

## 🔧 Project Workflow

1. Data Cleaning & Preprocessing
2. Feature Engineering (Car Age, Encoding)
3. Model Training (Random Forest)
4. Model Evaluation
5. Model Saving (`.pkl`)
6. Web App Development (Streamlit)
7. Deployment on Streamlit Cloud

---

## 📁 Project Structure
Car Price Prediction/
│
├── app.py
├── final_model.pkl
├── columns.pkl
├── Car Dataset Processed.csv
├── requirements.txt
└── models.ipynb


---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction

pip install -r requirements.txt
streamlit run app.py
