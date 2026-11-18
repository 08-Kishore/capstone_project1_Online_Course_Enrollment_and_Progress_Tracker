import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

def run_databricks_etl():
    spark = SparkSession.builder \
        .appName("OnlineCourse_Databricks_ETL") \
        .getOrCreate()

    print("Spark Session initialized successfully.")
    data_path = "data/"
    
    students_df = spark.read.option("header", "true").inferSchema(True).csv(os.path.join(data_path, "students.csv"))
    courses_df = spark.read.option("header", "true").inferSchema(True).csv(os.path.join(data_path, "courses.csv"))
    enrollments_df = spark.read.option("header", "true").inferSchema(True).csv(os.path.join(data_path, "enrollments.csv"))
    progress_df = spark.read.option("header", "true").inferSchema(True).csv(os.path.join(data_path, "progress.csv"))

    print("Raw datasets loaded into Spark DataFrames.")

    final_df = students_df \
        .join(enrollments_df, "student_id", "inner") \
        .join(courses_df, "course_id", "inner") \
        .join(progress_df, "enrollment_id", "inner")

    cleaned_etl_df = final_df.select(
        col("student_name"),
        col("course_name"),
        col("department"),
        to_date(col("enrollment_date"), "yyyy-MM-dd").alias("enrollment_date"),
        col("status"),
        col("score")
    ).na.fill({"score": 0.0, "status": "enrolled"})

    print("\n--- Consolidated Final ETL Table Preview ---")
    cleaned_etl_df.show(10, truncate=False)

    output_dir = "week4_databricks"
    os.makedirs(output_dir, exist_ok=True)
    
    csv_output_path = os.path.join(output_dir, "final_clean_output.csv")
    
    cleaned_etl_df.toPandas().to_csv(csv_output_path, index=False)
    
    print(f"ETL pipeline execution complete! Final clean output saved to {csv_output_path}")

if __name__ == "__main__":
    run_databricks_etl()