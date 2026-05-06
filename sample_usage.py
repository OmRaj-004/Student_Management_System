\"
Sample usage of the Student Management System
This script demonstrates programmatic usage of the system
\"

from database import StudentDatabase
from reports import ReportGenerator

# Create a database instance
db = StudentDatabase()

# Add some sample students
print("Adding sample students...")
db.add_student("S001", "Alice Johnson", 92, 95)
db.add_student("S002", "Bob Smith", 85, 88)
db.add_student("S003", "Carol Davis", 78, 90)
db.add_student("S004", "David Brown", 95, 92)
db.add_student("S005", "Eva Martinez", 88, 85)

print("Students added successfully!\n")

# Display all students
print("All Students:")
for student in db.get_all_students():
    print(f"  {student}")

print(f"\nTotal Students: {db.get_total_students()}\n")

# Search for a student
print("Searching for student with roll number S002:")
student = db.search_student("S002")
if student:
    print(f"  Found: {student}\n")

# Search by name
print("Searching for students with name 'David':")
results = db.search_by_name("David")
for result in results:
    print(f"  {result}\n")

# Update a student
print("Updating student S003...")
db.update_student("S003", marks=82, attendance=92)
updated_student = db.search_student("S003")
print(f"  Updated: {updated_student}\n")

# Generate reports
report_gen = ReportGenerator(db)

print("=" * 60)
print("GENERATING REPORTS")
print("=" * 60)

print(report_gen.generate_class_report())
print(report_gen.generate_toppers_report())
print(report_gen.generate_attendance_report())
print(report_gen.generate_marks_report())

print("Sample usage completed!")
