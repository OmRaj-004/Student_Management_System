# Student Management System - Quick Start Guide

## Getting Started in 3 Steps

### Step 1: Run the Application
\\\ash
python main.py
\\\

### Step 2: Add Your First Student
- Select option **1** from the menu
- Enter Roll Number (e.g., 101)
- Enter Student Name (e.g., John Doe)
- Enter Marks (0-100)
- Enter Attendance (0-100)

### Step 3: Explore Features
- **View all students** → Option 5
- **Search for a student** → Option 2
- **Update records** → Option 3
- **Generate reports** → Option 6

## Common Tasks

### To Add a New Student
1. Press **1**
2. Fill in all required details
3. System confirms: "Student added successfully!"

### To Search for a Student
1. Press **2**
2. Choose to search by **Roll Number** (1) or **Name** (2)
3. Enter search term
4. Student details appear

### To Update a Student Record
1. Press **3**
2. Enter the student's roll number
3. Update only the fields you want to change
4. Leave blank to keep current values

### To Delete a Student
1. Press **4**
2. Enter the roll number
3. Confirm deletion (type "yes")

### To Generate a Report
1. Press **6**
2. Choose report type:
   - **Class Report** - Overview of all students
   - **Top Performers** - Best 5 students
   - **Attendance Report** - Attendance analysis
   - **Marks Distribution** - Grade-wise breakdown
3. Optionally save report to file

## Report Descriptions

### Class Report
Shows all students with their complete details and statistics:
- Individual student information
- Total student count
- Average marks across the class
- Average attendance percentage

### Top Performers Report
Lists the 5 highest-scoring students in descending order by marks.

### Attendance Report
Categorizes students into two groups:
- Students with good attendance (75% or more)
- Students with poor attendance (less than 75%)

### Marks Distribution Report
Shows how many students fall in each grade category:
- Grade A: 90-100 marks
- Grade B: 80-89 marks
- Grade C: 70-79 marks
- Grade D: 60-69 marks
- Grade F: Below 60 marks

## Data Storage

- All student data is saved automatically in **students.json**
- No manual backup needed
- Data persists between sessions
- Reports can be exported to text files

## Tips & Tricks

1. **Search Tip**: When searching by name, you can enter partial names (e.g., "John" will find "John Doe")

2. **Batch Export**: Generate a report and save it with a descriptive name for future reference

3. **Data Import**: You can manually edit the students.json file to import bulk data

4. **Sample Data**: Use sample_usage.py to understand the system's capabilities

## Troubleshooting

### "Student with this roll number already exists"
- The roll number is already in use
- Choose a different roll number

### "Marks must be between 0 and 100"
- Ensure marks are entered as a number between 0 and 100
- Use decimal numbers if needed (e.g., 85.5)

### "Invalid choice! Please try again"
- Enter a number from the available options
- Check the menu display

## File Structure

- **main.py** - Run this file to start the application
- **student.py** - Student data model
- **database.py** - Database operations
- **reports.py** - Report generation
- **students.json** - Your data (auto-created)

---

Happy managing! For more details, see README.md
