# Smart Attendance System using Python

students = {}

def add_student():
roll_no = input("Enter Roll Number: ")
name = input("Enter Student Name: ")

```
students[roll_no] = {
    "name": name,
    "present": 0,
    "total": 0
}

print(f"{name} added successfully!")
```

def mark_attendance():
if not students:
print("No students available.")
return

```
print("\n===== MARK ATTENDANCE =====")

for roll_no, student in students.items():
    print(f"\nRoll No: {roll_no}_
```
