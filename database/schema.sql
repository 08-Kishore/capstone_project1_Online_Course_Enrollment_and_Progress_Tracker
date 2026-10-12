-- Create and use the database
CREATE DATABASE IF NOT EXISTS online_course_db;
USE online_course_db;

-- Drop tables if they exist to allow clean re-runs
DROP TABLE IF EXISTS progress;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;

-- 1. Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- 2. Courses Table
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL
);

-- 3. Enrollments Table (with indexes for fast student/course lookup)
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

CREATE INDEX idx_student ON enrollments(student_id);
CREATE INDEX idx_course ON enrollments(course_id);

-- 4. Progress Table
CREATE TABLE progress (
    progress_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    status ENUM('enrolled', 'in_progress', 'completed', 'dropped') DEFAULT 'enrolled',
    score DECIMAL(5,2) NULL,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
);

-- 5. Stored Procedure: Calculate course completion percentage for a student
DELIMITER //

CREATE PROCEDURE student_completion_rate(IN s_id INT)
BEGIN
    DECLARE total INT DEFAULT 0;
    DECLARE completed INT DEFAULT 0;
    
    -- Get total enrollments for the student
    SELECT COUNT(*) INTO total 
    FROM enrollments e 
    JOIN progress p ON e.enrollment_id = p.enrollment_id 
    WHERE e.student_id = s_id;
     
    -- Get total completed courses for the student
    SELECT COUNT(*) INTO completed
    FROM enrollments e 
    JOIN progress p ON e.enrollment_id = p.enrollment_id 
    WHERE e.student_id = s_id AND p.status = 'completed';
    
    -- Output the completion percentage (handles division by zero check optionally or returns NULL/0)
    IF total > 0 THEN
        SELECT (completed * 100.0 / total) AS completed_percentage;
    ELSE
        SELECT 0.0 AS completed_percentage;
    END IF;
END //

DELIMITER ;