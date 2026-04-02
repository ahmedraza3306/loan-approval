# Loan Approval Prediction System

## 📌 Overview

This project is a Machine Learning-based system that predicts whether a loan application will be **approved or rejected** based on applicant details such as income, loan amount, CIBIL score, employment status, and existing loans.

The model uses a **Decision Tree Classifier**, which provides simple and interpretable decision-making.

---

## 🚀 Features

* Takes real-time user input
* Predicts loan approval status
* Uses Decision Tree algorithm
* Simple and easy-to-understand implementation

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

## 📂 Project Structure

loan-approval-ml/
│
├── lpc.py
├── README.md
└── requirements.txt

---

## ⚙️ How to Run

### Step 1: Install dependencies

pip install pandas numpy scikit-learn

### Step 2: Run the program

python lpc.py

---

## 📊 Input Parameters

* **Income** – Applicant’s income
* **Loan Amount** – Requested loan amount
* **CIBIL Score** – Credit score
* **Employment** – 1 = Employed, 0 = Not employed
* **Existing Loan** – 1 = Has existing loan, 0 = No loan

---

## ✅ Example

### Input:

Income: 60000
Loan Amount: 200000
CIBIL: 750
Employment: 1
Existing Loan: 0

### Output:

Loan Approved ✅

---

## 📈 Model Details

* Algorithm: Decision Tree Classifier
* Train-Test Split: 80% Training, 20% Testing
* Evaluation Metric: Accuracy Score

---

## ⚠️ Limitations

* Uses a small dataset (for demonstration)
* Accuracy may vary
* Not suitable for real-world financial decisions without large data

---

## 🔮 Future Improvements

* Use larger real-world dataset
* Improve accuracy using Random Forest
* Build a web interface (Flask/Streamlit)
* Add visualization and feature importance

---

## 👨‍💻 Author

**Deputy Ahmed Raza**
Reg No: 2023004017

---

## 📌 Conclusion

This project demonstrates how machine learning can be used for decision-making in financial systems. It provides a simple and understandable approach to loan approval prediction.
