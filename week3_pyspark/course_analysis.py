from pyspark.sql import SparkSession

def run_spark_analysis():
    spark = SparkSession.builder.appName("CourseAnalysis").getOrCreate()
    
    enrollments_df = spark.read.option("header", "true").csv("data/enrollments.csv")
    progress_df = spark.read.option("header", "true").csv("data/progress.csv")
    courses_df = spark.read.option("header", "true").csv("data/courses.csv")
    
    joined_df = enrollments_df.join(progress_df, "enrollment_id").join(courses_df, "course_id")
    
    summary_df = joined_df.groupBy("course_name").count()
    summary_df.show()

if __name__ == "__main__":
    run_spark_analysis()