<<<<<<< HEAD
Online Course Enrollment and Progress Tracker
📌 Week 1: Database Foundations (MySQL & MongoDB)
Welcome to Week 1 of the Online Course Enrollment and Progress Tracker capstone project. This phase establishes the core database architecture, combining relational data management (MySQL) for structured entities and document storage (MongoDB) for flexible student reviews.

🎯 Objectives & Accomplishments
MySQL Relational Database: Designed and initialized a structured database (online_course_db) with relational tables for students, courses, enrollments, and progress tracking.

Performance Optimization: Created optimized table indexes (idx_student, idx_course) to ensure rapid lookup speeds for enrollment queries.

Business Logic Automation: Implemented a MySQL stored procedure (student_completion_rate) to dynamically compute a student's course completion percentage.

NoSQL Feedback Integration: Utilized MongoDB to ingest and store unstructured student review data via JSON files, complete with collection indexing for high-performance searching.

Modular Python Configuration: Established a clean project layout separating database configurations, raw CSV/JSON datasets, and setup scripts.

📁 Project File Structure
Plaintext
capstone1_online_course_enrollment/
│
├── .venv/                      # Python Virtual Environment
├── config/
│   ├── __init__.py
│   ├── mysql_db.py           # MySQL connection handler
│   └── mongo_db.py           # MongoDB connection handler
│
├── data/                       # Week 1: Raw Datasets (CSV & JSON)
│   ├── students.csv
│   ├── courses.csv
│   ├── enrollments.csv
│   ├── progress.csv
│   └── feedback.json         # MongoDB student reviews dataset
│
├── database/
│   └── schema.sql            # MySQL schema, foreign keys, indexes, & stored procedure
│
├── week1_database/
│   └── seed_feedback.py      # Python script to load JSON feedback into MongoDB & build indexes
│
├── .env                        # Secure environment variables (Credentials & URIs)
├── requirements.txt            # Project dependencies (pymongo, mysql-connector-python, pandas, etc.)
└── README.md                   # Project documentation
🛠️ Getting Started & Installation
1. Clone or Open the Project Workspace
Navigate to your project directory in your terminal:

PowerShell
cd path/to/capstone1_online_course_enrollment
2. Set Up the Virtual Environment
Activate your Python virtual environment:

PowerShell
.venv\Scripts\Activate.ps1
3. Install Dependencies
Install all required Python libraries via pip:

PowerShell
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory with your local database credentials:

Code snippet
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=online_course_db

MONGO_URI=mongodb://localhost:27017/
MONGO_DB_NAME=online_course_db
🚀 Week 1 Deliverables Execution
Run MySQL Schema Script:
Execute the database/schema.sql script inside your MySQL client (or Workbench) to generate your relational tables, indexes, and the student_completion_rate stored procedure.

Seed MongoDB Feedback Data:
Run the Python MongoDB seeding script to load JSON feedback and configure search indexes:

PowerShell
python week1_database/seed_feedback.py
🔜 Next Steps (Week 2 Preview)
Data Preprocessing in Python: Load relational data using pandas and NumPy, clean missing values/percentages, and compute initial course-level analytics.
=======
# capstone_project1_Online_Course_Enrollment_and_Progress_Tracker
>>>>>>> b26dd05114047c03bc3cea8d1a72b15325220814
