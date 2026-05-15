# Student Login Project Sample

## How the Decorator Is Used

The decorator `log_activity` is defined in `decorators.py` and applied with `@log_activity`
above each user-facing function in `users.py`.

Decorated functions:
- `student_login(username)`
- `submit_assignment(username, assignment)`
- `view_grades(username)`

When `main.py` calls one of these functions, the following execution order occurs:
1. The wrapper prints a separator line.
2. The wrapper prints the original function name using `func.__name__`.
3. The wrapper prints the current timestamp.
4. The wrapper prints `Activity started...`.
5. The wrapper calls the original function using `func(*args, **kwargs)`.
6. The original function prints its business message.
7. Control returns to the wrapper.
8. The wrapper prints `Activity completed.` and returns the result.

## Debugging Process

I debugged the program by tracing the call path from `main.py` to `users.py` and then into
`decorators.py`.

Observations from running the program:
- Each function call in `main.py` produced a full logging block.
- The business message appeared between `Activity started...` and `Activity completed.`.
- `submit_assignment` confirmed that the decorator correctly forwards multiple arguments.
- The output proved that the decorator adds behavior before and after the original function
  without changing the original function bodies.

Example output pattern:

```text
===================================
Function: student_login
Time: 2026-05-16 09:03:26.851756
Activity started...
Mohammad logged into the system.
Activity completed.
===================================

===================================
Function: submit_assignment
Time: 2026-05-16 08:56:31.440037
Activity started...
Mohammad submitted Python Decorator Project.
Activity completed.
===================================

===================================
Function: view_grades
Time: 2026-05-16 08:56:31.440052
Activity started...
Alex is viewing grades.
Activity completed.
===================================

```

## Findings

The decorator works correctly. It prints extra logging messages before and after each
student action.

There is one logic problem in the example. `Alex` can view grades without logging in
first. In a real system, a user should log in before viewing grades.

The logging messages come from the decorator, not from the functions in `users.py`.
