import pandas as pd


# Load the CSV file
df = pd.read_csv('student_scores.csv')
print("CSV loaded successfully!")
print(df.head())  # Shows first 5 rows

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing marks/attendance with 0
df['marks'] = df['marks'].fillna(0)
df['attendance'] = df['attendance'].fillna(0)

# Compute average marks and attendance per subject
summary = df.groupby('subject')[['marks', 'attendance']].mean().reset_index()
summary['marks'] = summary['marks'].round(2)
summary['attendance'] = summary['attendance'].round(2)

print("\nSummary (Average marks & attendance per subject):")
print(summary)

# Save summary to Excel
summary.to_excel('student_summary.xlsx', index=False)
print("\nSummary saved as 'student_summary.xlsx' successfully!")


