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

