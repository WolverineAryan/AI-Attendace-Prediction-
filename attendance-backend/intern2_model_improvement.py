import pandas as pd

df = pd.read_csv("data/attendance_extended_features.csv")

# Create reason column
df["Risk_Reason"] = df.apply(
    lambda row:
        "Very low attendance"
        if row["Attendance_Percentage"] < 60 else
        "High leaves and late days"
        if row["Impact_Score"] > 15 else
        "Normal",
    axis=1
)

# Save file
df.to_csv("data/attendance_with_reason.csv", index=False)

print("✅ attendance_with_reason.csv created")
