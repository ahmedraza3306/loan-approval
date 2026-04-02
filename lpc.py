import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


data = pd.DataFrame({
    "Income":[25000,40000,60000,30000,80000,50000,20000,70000,65000,45000],
    "LoanAmount":[200000,150000,300000,100000,400000,250000,120000,350000,280000,220000],
    "CIBIL":[650,720,780,600,800,750,580,790,710,690],
    "Employment":[1,1,1,0,1,1,0,1,1,1],  # 1=Employed
    "ExistingLoan":[0,1,0,1,0,0,1,0,0,1], # 1=Already has loan
    "Loan_Status":[0,1,1,0,1,1,0,1,1,0]  # 1=Approved
})

print("Dataset:")
print(data)



X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



model = DecisionTreeClassifier()

model.fit(X_train, y_train)



pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, pred))



print("\nEnter Applicant Details")

income = float(input("Enter Income: "))
loan_amount = float(input("Enter Loan Amount: "))
cibil = int(input("Enter CIBIL Score: "))
employment = int(input("Employment (1=Yes,0=No): "))
existing = int(input("Existing Loan (1=Yes,0=No): "))

applicant = np.array([[income,loan_amount,cibil,employment,existing]])

result = model.predict(applicant)


if result[0] == 1:
    print("\nLoan Approved")
else:
    print("\nLoan Rejected")