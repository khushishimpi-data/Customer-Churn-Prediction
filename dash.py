import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Load Pipeline
# --------------------------------------------------
pipeline = joblib.load("churn_pipeline.pkl")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("""
<h1 style='text-align:center;color:#22c55e;'>Customer Churn Intelligence</h1>
<p style='text-align:center;font-size:18px;'>
Probability-Based AI Retention System
</p>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# Sidebar Inputs
# --------------------------------------------------
st.sidebar.header("Customer Profile")

age = st.sidebar.slider("Age", 18, 90, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
tenure = st.sidebar.slider("Tenure (Months)", 0, 120, 12)
monthly = st.sidebar.slider("Monthly Charges", 30.0, 150.0, 70.0)

gender_val = 1 if gender == "Female" else 0

charges_per_tenure = monthly / (tenure + 1)
high_monthly = 1 if monthly > 80 else 0

# --------------------------------------------------
# Prediction Logic
# --------------------------------------------------
if st.button("Predict Churn Risk"):

    with st.spinner("Running churn risk analysis..."):
        time.sleep(1.5)

        input_df = pd.DataFrame([{
            "Age": age,
            "Gender": gender_val,
            "Tenure": tenure,
            "MonthlyCharges": monthly,
            "ChargesPerTenure": charges_per_tenure,
            "HighMonthlyCharge": high_monthly
        }])

        prob = pipeline.predict_proba(input_df)[0][1]

    st.metric("Churn Probability", f"{prob*100:.2f}%")

    if prob >= 0.75:
        st.error("🚨 HIGH RISK CUSTOMER")
        st.write("""
        **Recommended Actions**
        - Immediate retention call  
        - Personalized discount offer  
        - Priority customer support  
        """)
    elif prob >= 0.40:
        st.warning("⚠️ MEDIUM RISK CUSTOMER")
        st.write("""
        **Recommended Actions**
        - Engagement emails  
        - Loyalty incentives  
        - Usage monitoring  
        """)
    else:
        st.success("✅ LOW RISK CUSTOMER")
        st.write("""
        **Recommended Actions**
        - Maintain service quality  
        - Upsell premium plans  
        - Encourage referrals  
        """)

st.divider()
st.markdown("<p style='text-align:center;'>Academic & Industry Grade ML System</p>", unsafe_allow_html=True)
