# ==================================================
# INTERN 1 - DATA CLEANING, FEATURE ENGINEERING & EDA
# ==================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# STEP 1: Load dataset
# --------------------------------------------------

df = pd.read_csv("data/clean_attendance_data.csv")

print("\n========== RAW DATA ==========\n")
print(df.head())

# --------------------------------------------------
# STEP 2: DATA CLEANING
# --------------------------------------------------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values with 0
df.fillna(0, inplace=True)

print("\n========== DATA INFO AFTER CLEANING ==========\n")
print(df.info())

# --------------------------------------------------
# STEP 3: FEATURE ENGINEERING (NEW COLUMNS)
# --------------------------------------------------

# Convert Present / Absent → Numeric
df["Risk"] = df["Final_Status"].map({
    "Present": 0,
    "Absent": 1
})

# Discipline score = Late days + Leaves
df["Discipline_Score"] = df["Late_Days"] + df["Leaves"]

# Attendance-based risk
df["Attendance_Risk"] = df["Attendance_Percentage"].apply(
    lambda x: 1 if x < 75 else 0
)

print("\n========== DATA AFTER NEW COLUMNS ==========\n")
print(df.head())

# --------------------------------------------------
# STEP 4: FINAL CLEAN DATASET
# --------------------------------------------------

final_df = df[
    [
        "Student_ID",
        "Attendance_Percentage",
        "Late_Days",
        "Leaves",
        "Discipline_Score",
        "Attendance_Risk",
        "Risk"
    ]
]

# Save cleaned dataset
final_df.to_csv("data/final_clean_attendance_data.csv", index=False)

print("\n✅ Final cleaned dataset saved successfully\n")

# --------------------------------------------------
# STEP 5: EXPLORATORY DATA ANALYSIS (EDA)
# --------------------------------------------------

sns.set(style="whitegrid")

# 1. Attendance Percentage Distribution
plt.figure(figsize=(8, 5))
sns.histplot(final_df["Attendance_Percentage"], bins=10, kde=True)
plt.title("Attendance Percentage Distribution")
plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")
plt.show()

# 2. Risk Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(x="Risk", data=final_df)
plt.title("Attendance Risk Count")
plt.xlabel("Risk (0 = Safe, 1 = High Risk)")
plt.ylabel("Count")
plt.show()

# 3. Late Days vs Risk
plt.figure(figsize=(6, 4))
sns.boxplot(x="Risk", y="Late_Days", data=final_df)
plt.title("Late Days vs Attendance Risk")
plt.show()

# 4. Leaves vs Risk
plt.figure(figsize=(6, 4))
sns.boxplot(x="Risk", y="Leaves", data=final_df)
plt.title("Leaves vs Attendance Risk")
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    final_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.show()

print("\n✅ EDA Completed Successfully")
