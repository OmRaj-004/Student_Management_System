# Student Management System

A comprehensive Python-based application for managing student records and generating reports.

## Features

### 1. **Store Student Details**
   - Roll Number
   - Name
   - Marks (0-100)
   - Attendance Percentage (0-100)

### 2. **Search and Update Records**
   - Search students by Roll Number
   - Search students by Name
   - Update student information (name, marks, attendance)
   - Delete student records
   - View all students in the system

### 3. **Database Storage**
   - Student records are saved in a local SQLite database file (`students.db`)
   - No external dependencies required beyond Python standard library

### 4. **GUI Interface**
   - Tkinter-based graphical user interface
   - Add, update, delete, and search student records from the app window
   - View all students in a sortable table
   - Generate reports via buttons and save them to text files

### 5. **Generate Reports**
   - **Class Report**: Complete overview of all students with average marks and attendance
   - **Top Performers Report**: Top 5 students by marks
   - **Attendance Report**: Students with good and poor attendance
   - **Marks Distribution Report**: Grade-wise distribution (A, B, C, D, F)
   - Export reports to text files

## Project Structure

\\\
Student_Management_System/
├── main.py              # Main entrypoint for GUI application
├── gui.py               # Tkinter graphical interface
├── student.py           # Student class definition
├── database.py          # SQLite database operations and persistence
├── reports.py           # Report generation functionality
├── students.db          # Local SQLite data file (created on first run)
└── README.md           # Project documentation
\\\

## Installation and Usage

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the Application

1. Navigate to the project directory:
   \\\ash
   cd Student_Management_System
   \\\

2. Run the application:
   \\\ash
   python main.py
   \\\

3. Follow the on-screen menu to:
   - Add new students
   - Search for students
   - Update student records
   - Delete students
   - Generate various reports

## Menu Options

1. **Add Student** - Add a new student with details
2. **Search Student** - Search by roll number or name
3. **Update Student** - Modify existing student information
4. **Delete Student** - Remove a student record
5. **View All Students** - Display all students in the system
6. **Generate Reports** - Access various reporting options
7. **Exit** - Close the application

## Report Types

### Class Report
Shows:
- All students with their details
- Total number of students
- Average marks
- Average attendance percentage

### Top Performers Report
Shows the top 5 students ranked by marks in descending order

### Attendance Report
Categorizes students as:
- Good Attendance (>= 75%)
- Poor Attendance (< 75%)

### Marks Distribution Report
Shows grade distribution:
- Grade A: Marks >= 90
- Grade B: Marks 80-89
- Grade C: Marks 70-79
- Grade D: Marks 60-69
- Grade F: Marks < 60

## Data Storage

Student data is automatically saved to an SQLite database file named `students.db` in the project directory. This ensures data persistence between application sessions.

## Example Usage

1. Start the application
2. Add several students
3. View all students in the table
4. Search for a specific student by roll number or name
5. Update a student's marks or attendance
6. Generate reports to analyze student performance
7. Save reports to text files for sharing

## Features Highlights

- **Input Validation**: Ensures valid data entry (marks and attendance between 0-100)
- **Duplicate Prevention**: Prevents adding students with duplicate roll numbers
- **Easy Updates**: Update specific fields without affecting others
- **Export Capability**: Save generated reports to text files
- **User-Friendly**: Tkinter-based GUI interface
- **Persistent Storage**: All data is saved to a local SQLite database

## Technical Details

- Built with Python 3
- Uses SQLite for persistent data storage
- Object-oriented design with Student, Database, GUI, and ReportGenerator components
- No external library dependencies beyond Python standard library

## Future Enhancements

- Export report selection by report type
- Student performance analytics and charts
- Role-based access and login support
- Improved filtering and sorting in the GUI table

- Graphical charts for data visualization
- User authentication and roles

## Author Notes

This system provides a simple yet effective way to manage student records in educational institutions. It can be extended with additional features based on specific requirements.

---

**Version**: 1.0
**Created**: April 2026
**License**: Open Source
