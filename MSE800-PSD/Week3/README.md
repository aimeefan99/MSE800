# Week 3 - Activity 1: Student-Course Database Design

## ER Diagram Description

This ER diagram represents a simple database design for managing students and courses in an educational system.

### Entities:

1. **STUDENT**
   - `student_id` (Primary Key): Unique identifier for each student
   - `student_name`: Student's full name

2. **COURSE**
   - `course_id` (Primary Key): Unique identifier for each course
   - `course_name`: Name of the course

3. **ENROLLMENT**
   - `student_id` (Foreign Key): References STUDENT.student_id
   - `course_id` (Foreign Key): References COURSE.course_id
   - `enrollment_date`: Date when the student enrolled in the course

### Relationships:

- **STUDENT** to **ENROLLMENT**: One-to-many (a student can enroll in multiple courses)
- **COURSE** to **ENROLLMENT**: One-to-many (a course can have multiple enrolled students)
- This creates a many-to-many relationship between students and courses through the ENROLLMENT entity

### Sample Course List

In this design, three example courses are included:

- `MSE800` - Software Development
- `MSE801` - Research Methods
- `MSE802` - Quantum Computing

Each course is represented by a `COURSE` record with a unique `course_id`, a course name, and a description.

### SQL Commands Summary for Student-Course Database

Here's a concise summary of the SQL commands used to create and populate the database:

#### Table Creation
```sql
-- Create STUDENT table
CREATE TABLE STUDENT (
    student_id VARCHAR(20) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL
);

-- Create COURSE table  
CREATE TABLE COURSE (
    course_id VARCHAR(20) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- Create ENROLLMENT table (junction table for many-to-many relationship)
CREATE TABLE ENROLLMENT (
    student_id VARCHAR(20),
    course_id VARCHAR(20),
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id),
    FOREIGN KEY (course_id) REFERENCES COURSE(course_id)
);
```

#### Data Insertion
```sql
-- Insert course data
INSERT INTO COURSE (course_id, course_name) VALUES
('MSE800', 'Software Development'),
('MSE801', 'Research Methods'),
('MSE802', 'Quantum Computing');

-- Insert lecturer data
INSERT INTO LECTURER (lecturer_id, lecturer_name, lecturer_department, lecturer_email, course_id) VALUES
('L001', 'Dr. Mohammad', 'Computer Science', 'mohammad@university.edu', 'MSE800'),
('L002', 'Dr. Reem', 'Research', 'reem@university.edu', 'MSE801'),
('L003', 'Dr. Arun', 'Computer Science', 'arun@university.edu', 'MSE802');

-- Insert student data
INSERT INTO STUDENT (student_id, student_name) VALUES
('S001', 'Aria'),
('S002', 'Bob'),
('S003', 'Carmen');

-- Insert enrollment data (all students enrolled in all courses)
INSERT INTO ENROLLMENT (student_id, course_id, enrollment_date) VALUES
('S001', 'MSE800', '2026-04-07'),
('S001', 'MSE801', '2026-04-07'),
('S001', 'MSE802', '2026-04-07'),
('S002', 'MSE800', '2026-04-07'),
('S002', 'MSE801', '2026-04-07'),
('S002', 'MSE802', '2026-04-07'),
('S003', 'MSE800', '2026-04-07'),
('S003', 'MSE801', '2026-04-07'),
('S003', 'MSE802', '2026-04-07');
```

#### Verification Commands
```sql
-- Check if tables exist
.tables

-- View table structure
PRAGMA table_info(STUDENT);
PRAGMA table_info(COURSE);
PRAGMA table_info(LECTURER);
PRAGMA table_info(ENROLLMENT);

-- Count records in each table
SELECT COUNT(*) FROM STUDENT;
SELECT COUNT(*) FROM COURSE;
SELECT COUNT(*) FROM LECTURER;
SELECT COUNT(*) FROM ENROLLMENT;

-- View all data
SELECT * FROM STUDENT;
SELECT * FROM COURSE;
SELECT * FROM LECTURER;
SELECT * FROM ENROLLMENT;
```
