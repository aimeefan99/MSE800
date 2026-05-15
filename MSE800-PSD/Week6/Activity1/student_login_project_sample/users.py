from decorators import log_activity

# This module contains the functions related to student activities such as logging in, submitting assignments, and viewing grades. 
# Each function is decorated with the log_activity decorator to log the activity details whenever the function is called.

#   This function allows a student to log in. 
#   It takes the username as a parameter and prints a message indicating that the user has logged in.
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")

#   This function allows a student to submit an assignment. 
#   It takes the username and the assignment name as parameters and prints a message indicating that the assignment has been submitted.
@log_activity
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")

#   This function allows a student to view their grades.
#   It takes the username as a parameter and prints a message indicating that the user is viewing their grades.
@log_activity
def view_grades(username):
    print(f"{username} is viewing grades.")
