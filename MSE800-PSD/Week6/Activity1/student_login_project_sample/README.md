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
```

## Findings

The project uses decorators well to separate logging from the main student actions.
This makes the code easier to maintain because the logging logic is written once and reused
for multiple functions.

One important debugging conclusion is that the decorator is responsible for the extra output,
not the functions in `users.py`. If a future bug appears in the logging sequence, the first
place to inspect should be the `wrapper` inside `log_activity`.

Another useful observation is that this example does not use `functools.wraps`, so metadata
such as the original function name object can be partially hidden by the wrapper in more
advanced cases. The current example still works because it prints `func.__name__` from the
closure, but adding `@wraps(func)` would make the decorator more complete.

There is also a small logic issue in the sample flow: `Alex` is able to call
`view_grades()` without logging in first. This does not break the program because the
current project only prints messages and does not validate login state, but in a real
system this would be considered a logic flaw.
