# ==========================================
# INTERN 2 - MACHINE LEARNING MODEL
# Attendance Risk Prediction
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --------------------------------------------------
# STEP 1: Load cleaned dataset
# --------------------------------------------------

df = pd.read_csv("data/final_clean_attendance_data.csv")

print("\nDataset Loaded Successfully\n")
print(df.head())

# --------------------------------------------------
# STEP 2: Feature selection & target
# --------------------------------------------------

X = df[
    [
        "Attendance_Percentage",
        "Late_Days",
        "Leaves",
        "Discipline_Score",
        "Attendance_Risk"
    ]
]

y = df["Risk"]

# --------------------------------------------------
# STEP 3: Train–Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining rows:", X_train.shape[0])
print("Testing rows:", X_test.shape[0])

# --------------------------------------------------
# STEP 4: Logistic Regression
# --------------------------------------------------

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

labels = [0, 1]

print("\n===== LOGISTIC REGRESSION =====")
print("Accuracy:", accuracy_score(y_test, lr_pred))
print("Confusion Matrix:\n",
      confusion_matrix(y_test, lr_pred, labels=labels))
print("Classification Report:\n",
      classification_report(y_test, lr_pred, labels=labels, zero_division=0))

# --------------------------------------------------
# STEP 5: Random Forest
# --------------------------------------------------

rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("\n===== RANDOM FOREST =====")
print("Accuracy:", accuracy_score(y_test, rf_pred))
print("Confusion Matrix:\n",
      confusion_matrix(y_test, rf_pred, labels=labels))
print("Classification Report:\n",
      classification_report(y_test, rf_pred, labels=labels, zero_division=0))

# --------------------------------------------------
# STEP 6: Save final model
# --------------------------------------------------

joblib.dump(rf_model, "model/attendance_risk_model.pkl")

print("\n✅ Final ML model saved successfully")
