#   This is the main file for the student login project. 
#   It will import the necessary functions from the users module and execute them in a sequence to demonstrate the student login activities.
from users import (
    student_login,
    submit_assignment,
    view_grades
)

# This is the main function that will execute the student login activities.
def main(): 

    # This will log in the student named Mohammad.
    student_login("Mohammad") 
    
    # This will submit an assignment for the student named Mohammad.
    submit_assignment( 
        "Mohammad",
        "Python Decorator Project"
    )
    
    # This will allow the student named Alex to view their grades.
    view_grades("Alex") 

#   This will ensure that the main function is called when the script is executed.
if __name__ == "__main__":
    main()
