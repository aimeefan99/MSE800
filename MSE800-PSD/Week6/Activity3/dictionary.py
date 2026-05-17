
number = [1,2,3,4,5] # This is a list of numbers from 1 to 5. It will be used in the dictionary comprehension to create a dictionary of squares.
squares={str(n): n**2 for n in number} # This is a dictionary comprehension that creates a dictionary called squares.

dict1 = {'a': 1, 'b': 2, 'c': 3} 
dict2 = {'c': 4, 'd': 5, 'e': 6} 
mapped_dict = {**dict1, **dict2} # This line merges the two dictionaries dict1 and dict2 into a single dictionary called mapped_dict using the unpacking operator (**).
print(mapped_dict) # This line prints the mapped_dict dictionary to the console, allowing us to

# Develop an script to be able to merge following dictionaries with condition of name with "ex" pattern        
# Dictionary 1
student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}
 
# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}
 
# Dictionary 3
student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}

merged_students = {
                    **({k: v for k, v in student1.items() if k == 'name' and "ex" in str(v)}),
                    **({k: v for k, v in student2.items() if k == 'name' and "ex" in str(v)}),
                    **({k: v for k, v in student3.items() if k == 'name' and "ex" in str(v)})
                  }
print(merged_students) 

