import os
import pandas as pd
import numpy as np

def clean_enrollment_data():
    print("Starting data cleaning process...")
    
    # Define file paths
    progress_path = os.path.join("data", "progress.csv")
    enrollments_path = os.path.join("data", "enrollments.csv")
    
    if not os.path.exists(progress_path) or not os.path.exists(enrollments_path):
        print("Error: Required CSV files not found in data/ directory.")
        return
    
    # 1. Load Datasets
    progress_df = pd.read_csv(progress_path)
    enrollments_df = pd.read_csv(enrollments_path)
    
    # 2. Clean 'progress.csv'
    # Fill missing score values with 0.0 for tracking purposes
    progress_df['score'] = progress_df['score'].fillna(0.0)
    
    # Use NumPy to clip scores between 0 and 100 to ensure validity
    progress_df['score'] = np.clip(progress_df['score'], 0, 100)
    
    # Fill any missing status fields with 'enrolled'
    progress_df['status'] = progress_df['status'].fillna('enrolled')
    
    # 3. Clean 'enrollments.csv'
    # Drop rows where student_id or course_id are missing
    enrollments_df = enrollments_df.dropna(subset=['student_id', 'course_id'])
    
    # Ensure enrollment_date is properly formatted as datetime
    enrollments_df['enrollment_date'] = pd.to_datetime(enrollments_df['enrollment_date'], errors='coerce')
    
    # 4. Merge datasets for comprehensive view
    merged_df = pd.merge(enrollments_df, progress_df, on='enrollment_id', how='inner')
    
    # Save cleaned output
    output_dir = "week2_preprocessing"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "cleaned_student_progress.csv")
    merged_df.to_csv(output_path, index=False)
    
    print(f"Data cleaning complete! Cleaned data saved to {output_path}")
    return merged_df

if __name__ == "__main__":
    clean_enrollment_data()