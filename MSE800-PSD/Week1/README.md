# Week1 - Power Calculator (MSE800-PSD)

## Project Description
This project is a simple Python program that calculates the power of a number (x^y).  
The program takes user input for base (x) and exponent (y), then returns the calculated result using Python's exponent operator.

---

## Project Structure

```
MSE800-PSD/
└── Week1/
    ├── power.py
    ├── testresult.png
    ├── README.md
```

---

## Environment Setup
- Operating System: macOS
- Python Environment: conda (demoEnv)
- Python Version: 3.8.20
- IDE: Visual Studio Code

---

## How to Run the Program
Activate the environment and run the script in terminal:
```bash
conda activate demoEnv
cd MSE800-PSD/Week1
python power.py
```
---

## Program Interaction (Test Cases)

### ✅ Positive Test Cases

**Test 1 Integer**
```text
Input:
Enter base (x): 3
Enter exponent (y): 3

Output:
3.0 to the power of 3.0 is 27.0
```
**Test 2 Float**
```text
Input:
Enter base (x): 3.5
Enter exponent (y): 2

Output:
3.5 to the power of 2.0 is 12.25
```
### ❌ Negative Test Cases

**Test 3 Letter**
```text
Input:
Enter base (x): a

Output:
Invalid input. Please enter numeric values.
```
**Test 4 Empty**
```text
Input:
Enter base (x):

Output:
Invalid input. Please enter numeric values.
```

