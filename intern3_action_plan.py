import pandas as pd

# Load dataset
df = pd.read_csv("data/attendance_with_reason.csv")

# -------------------------
# EARLY WARNING STUDENTS
# -------------------------
early_warning = df[
    (df["Attendance_Percentage"] >= 60) &
    (df["Attendance_Percentage"] < 75)
]

early_warning.to_csv(
    "data/early_warning_students.csv",
    index=False
)

# -------------------------
# ATTENDANCE SIMULATION
# -------------------------
df["Improved_Attendance"] = df["Attendance_Percentage"] + 10

df["Improved_Risk_Status"] = df["Improved_Attendance"].apply(
    lambda x: "Safe" if x >= 75 else "At Risk"
)

df.to_csv(
    "data/attendance_simulation.csv",
    index=False
)

print("✅ early_warning_students.csv created")
print("✅ attendance_simulation.csv created")
