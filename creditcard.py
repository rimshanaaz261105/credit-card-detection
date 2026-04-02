import streamlit as st
import joblib
import pandas as pd

# 1. Load the trained model
model = joblib.load('model.pkl')

# 2. UI Setup
st.set_page_config(page_title="FinFraud Detector", page_icon="💳")
st.title("🛡️ FinFraud Detector")
st.write("Enter transaction details to check for potential fraud.")

# 3. User Inputs (Simplified features)
st.subheader("Transaction Information")
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)
    old_balance = st.number_input("Sender Old Balance", min_value=0.0, value=500.0)

with col2:
    merchant_id = st.number_input("Merchant ID (Numeric)", min_value=0, value=1234)
    transaction_type = st.selectbox("Type", ["Transfer", "Payment", "Cash Out", "Debit"])

# 4. Prediction Logic
if st.button("Analyze Transaction"):
    # Convert inputs to a format the model understands (Match your training features!)
    # Note: This is a placeholder; real models need the exact columns used in training.
    features = pd.DataFrame([[amount, old_balance, merchant_id]], 
                           columns=['amount', 'oldbalanceOrg', 'merchant'])
    
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"🚨 High Risk! Fraud Probability: {probability:.2%}")
    else:
        st.success(f"✅ Transaction Safe. Fraud Probability: {probability:.2%}")
