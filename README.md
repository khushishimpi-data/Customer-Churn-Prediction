# 📊 Customer Churn Intelligence System  
### Probability-Based Machine Learning Solution for Customer Retention

---

## 📌 Project Overview

Customer churn is a major challenge for subscription-based businesses such as telecom, SaaS, banking, and digital services. Losing existing customers directly impacts revenue and long-term growth.

This project presents an **end-to-end Machine Learning system** that predicts **customer churn probability** and converts predictions into **actionable business insights** through an interactive **Streamlit web application**.

---

## 🎯 Objectives

- Predict **customer churn probability** rather than a simple Yes/No output  
- Engineer meaningful features that capture **customer behavior and value**  
- Build a **robust, production-ready ML pipeline**  
- Deploy an **interactive dashboard** for real-time churn analysis  
- Demonstrate **industry-grade ML practices** suitable for real-world use  

---

## 📂 Dataset Description

The dataset consists of **historical customer records** from a subscription-based business.

Each row represents **one customer**, and each column captures a specific attribute related to demographics, engagement, or billing behavior.

### 🔹 Key Features

| Feature | Description |
|------|-------------|
| Age | Customer age |
| Gender | Male / Female |
| Tenure | Number of months the customer has stayed |
| MonthlyCharges | Monthly billing amount |
| Churn | Target variable (1 = Yes, 0 = No) |

---

## 🧠 Feature Engineering

To enhance model performance and business relevance, additional features were created:

- **ChargesPerTenure**  
  ```text
  MonthlyCharges / (Tenure + 1)
Captures the cost burden relative to customer loyalty.

HighMonthlyCharge
Flags customers paying above the median monthly charge, identifying price-sensitive users.

Feature engineering plays a crucial role in improving churn prediction accuracy and interpretability.

🤖 Machine Learning Approach
🔹 Problem Type
Binary classification with probability-based output

🔹 Model Used
Random Forest Classifier

Why Random Forest?

Handles non-linear churn patterns

Robust to noise and outliers

Works well with engineered features

Produces reliable probability estimates

Minimal assumptions about data distribution

🔄 ML Pipeline (Production-Ready)
A single Scikit-Learn pipeline is used to ensure consistency and safe deployment.

mathematica
Copy code
Raw Data
   ↓
Feature Engineering
   ↓
Scaling (StandardScaler)
   ↓
Random Forest Classifier
   ↓
Churn Probability
This design prevents data leakage and ensures identical preprocessing during training and inference.

📊 Model Evaluation
The model is evaluated using multiple metrics:

ROC-AUC Score (~0.82) – primary metric

Precision, Recall, F1-Score

ROC-AUC is preferred because churn datasets are often imbalanced, and probability ranking is more valuable than raw accuracy.

📈 Churn Risk Segmentation
Predicted churn probabilities are converted into business-friendly risk levels:

Probability Range	Risk Level
≥ 75%	High Risk
40% – 75%	Medium Risk
< 40%	Low Risk

This enables targeted and cost-effective retention strategies.

🖥️ Streamlit Web Application
The project includes a high-end Streamlit dashboard that:

Accepts real-time customer inputs

Predicts churn probability instantly

Displays risk level clearly

Suggests actionable retention strategies

This bridges the gap between machine learning output and business decision-making.

🛠️ Technology Stack
Category	Tools
Language	Python
Data Processing	Pandas, NumPy
Machine Learning	Scikit-Learn
Model	Random Forest Classifier
Deployment	Streamlit
Model Storage	Joblib

📁 Project Structure
bash
Copy code
customer-churn-intelligence/
│
├── app.py                     # Streamlit application
├── churn_pipeline.pkl         # Trained ML pipeline
├── customer_churn_data.csv    # Dataset
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies
🚀 How to Run the Project
1️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
2️⃣ Run the Application
bash
Copy code
streamlit run app.py
🎓 Academic & Industry Relevance
This project demonstrates:

Strong understanding of churn analytics

Effective feature engineering

Probability-based ML modeling

End-to-end pipeline development

Real-world deployment using Streamlit

Business-oriented ML thinking
