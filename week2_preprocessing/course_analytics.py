import os
import pandas as pd
import numpy as np

def generate_course_analytics():
    cleaned_file = os.path.join("week2_preprocessing", "cleaned_student_progress.csv")
    courses_file = os.path.join("data", "courses.csv")
    
    if not os.path.exists(cleaned_file):
        print("Cleaned data file not found. Please run data_cleaning.py first.")
        return
        
    df = pd.read_csv(cleaned_file)
    courses_df = pd.read_csv(courses_file)
    
    # Merge with course names for readability
    full_df = pd.merge(df, courses_df, on='course_id', how='left')
    
    print("\n--- COURSE-LEVEL SUMMARY REPORT ---")
    
    # Group by course and compute key metrics using Pandas aggregation
    summary = full_df.groupby(['course_id', 'course_name', 'department']).agg(
        total_enrolled=('student_id', 'count'),
        completed_count=('status', lambda x: (x == 'completed').sum()),
        dropped_count=('status', lambda x: (x == 'dropped').sum()),
        average_score=('score', 'mean')
    ).reset_index()
    
    # Calculate completion rate percentage
    summary['completion_rate_%'] = (summary['completed_count'] / summary['total_enrolled']) * 100
    
    # Sort by completion rate descending
    summary = summary.sort_values(by='completion_rate_%', ascending=False)
    
    print(summary.to_string(index=False))
    
    # Save report
    report_path = os.path.join("week2_preprocessing", "course_summary_report.csv")
    summary.to_csv(report_path, index=False)
    print(f"\nCourse summary report successfully saved to {report_path}")

if __name__ == "__main__":
    generate_course_analytics()