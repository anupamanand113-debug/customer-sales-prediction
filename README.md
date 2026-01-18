# Customer Sales Prediction (ML + Streamlit)

This project predicts **Total Sales** based on customer purchase details using a **Machine Learning Regression model** and is deployed as a **Streamlit Web App**.

## Live Demo
 https://customer-sales-prediction-jfb4zvbfwgeib6ig3f2iom.streamlit.app/

---

## Features
- Predicts Total Sales based on:
  - Customer ID
  - Age
  - Quantity
  - Price
  - Gender
  - City
  - Product Category
- Trained using **Random Forest Regressor**
- Simple interactive UI using **Streamlit**
- Deployed online

---

##  Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit

---

##  Files in this Project
- `app.py` → Streamlit web app
- `sales_prediction_model.pkl` → trained ML model
- `training_columns.pkl` → saved feature columns
- `requirements.txt` → dependencies
- `customer_sales_dataset.csv` → dataset

---

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
