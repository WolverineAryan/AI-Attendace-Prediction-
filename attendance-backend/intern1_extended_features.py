import pandas as pd

df = pd.read_csv("data/final_clean_attendance_data.csv")

# -----------------------------
# New Features
# -----------------------------

df["Average_Attendance"] = df["Attendance_Percentage"]

df["Absence_Streak"] = df["Leaves"] + df["Late_Days"]

df["Low_Attendance_Flag"] = df["Attendance_Percentage"].apply(
    lambda x: 1 if x < 60 else 0
)

df["Impact_Score"] = (
    df["Late_Days"] * 0.4 +
    df["Leaves"] * 0.6
)

# Save new dataset
df.to_csv("data/attendance_extended_features.csv", index=False)

print("✅ Extended attendance features created successfully")
