# 🎓 Student Performance Analytics Project
Analyze and visualize student performance data using **Python**, **Excel**, and **Power BI**.  
This project identifies trends such as **average marks by subject**, **attendance impact on scores**, and **pass/fail distribution**.
##  Key Features

✅ **Data Cleaning & Analysis** — Process and summarize student data using Python (Pandas).  
✅ **Excel Integration** — Validate and visualize summarized data easily in Excel.  
✅ **Power BI Dashboard** — Build an interactive visual dashboard showcasing insights.  
✅ **Actionable Insights** — Understand learning trends and improvement areas.

##  How It Works

### 1️⃣ Environment Setup
Uses **Python 3.13+**, `pandas`, and `openpyxl` for data analysis.  
Install dependencies easily using:
```bash
pip install -r requirements.txt
2️⃣ Data Preparation

The dataset (student_scores.csv) contains:

Student ID

Name

Subject

Marks

Attendance

Pass/Fail status

Python script (analyze_scores.py) cleans the data and generates a summary (student_summary.xlsx) showing average marks and attendance per subject.

3️⃣ Dashboard Visualization

Import the summary file into Power BI to create:

📊 Clustered Column Chart (Average Marks per Subject)

🎯 Scatter Plot (Attendance vs Marks)

🍩 Donut Chart (Pass vs Fail Ratio)

Finally, export the dashboard as Student_Performance_Dashboard.pdf.

📊 Insights

📈 Students with higher attendance generally achieve better marks.
📘 Science shows the highest average marks.
📉 Math has improvement potential compared to other subjects.
🏆 Most students have passed overall.

🚀 Run the Project
Step 1: Clone this repository
git clone https://github.com/Sahana174/Student_Analytics_Project.git
cd Student_Analytics_Project

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Run the Python script
python analyze_scores.py

This will generate student_summary.xlsx.
Step 4: View Dashboard
Open student_summary.xlsx in Excel, or
Import it into Power BI and explore visuals interactively.

Who Can Benefit from This Project?

🎯 For Students: Understand performance and attendance relationships.
📚 For Educators: Identify subjects needing improvement.
💼 For Data Enthusiasts: Learn data analytics using Python, Excel, and Power BI.

Project Structure

student_scores.csv → Raw dataset containing student details, marks, and attendance
analyze_scores.py → Python script that cleans data and calculates summaries
student_summary.xlsx → Generated summary file (average marks and attendance)
Student_Performance_Dashboard.pdf → Power BI dashboard with visuals
requirements.txt → Python library dependencies
README.md → Project overview and setup guide

🛠️ Tools Used

🐍 Python (Pandas, OpenPyXL) – Data analysis and automation
📘 Excel – Data validation and tabular view
📈 Power BI – Interactive visualization and insights

🔗 Project Source Code

GitHub Repository: Student_Analytics_Project
