
import streamlit as st
import pandas as pd
import joblib

st.title("Customer Sales Prediction App")

# Load model + columns
model = joblib.load("sales_prediction_model.pkl")
training_columns = joblib.load("training_columns.pkl")

st.write("Enter customer purchase details to predict Total Sales")

# ✅ Input fields (smart limits)
customer_id = st.number_input("Customer ID", min_value=1, max_value=999999, value=1500)
age = st.number_input("Age", min_value=1, max_value=100, value=25)
quantity = st.number_input("Quantity", min_value=1, max_value=500, value=2)
price = st.number_input("Price per item", min_value=1, max_value=1000000, value=1000)

gender = st.selectbox("Gender", ["Male", "Female"])
city = st.selectbox("City", ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"])
category = st.selectbox("Product Category", ["Electronics", "Clothing", "Groceries", "Furniture"])

# Prepare input
input_data = pd.DataFrame([{
    "Customer_ID": customer_id,
    "Age": age,
    "Quantity": quantity,
    "Price": price,
    "Gender": gender,
    "City": city,
    "Product_Category": category
}])

# Encode input to match training columns
input_encoded = pd.get_dummies(input_data)
input_encoded = input_encoded.reindex(columns=training_columns, fill_value=0)

# Prediction
if st.button("Predict Sales"):
    prediction = model.predict(input_encoded)[0]
    st.success(f"Predicted Total Sales: ₹ {prediction:.2f}")
