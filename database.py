import os
import sqlite3
from student import Student

class StudentDatabase:
    """Handle student data persistence and operations"""

    def __init__(self, filename='students.db'):
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)
        self.connection.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        """Create the students table if it does not exist"""
        query = '''
        CREATE TABLE IF NOT EXISTS students (
            roll_no TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            marks REAL NOT NULL,
            attendance REAL NOT NULL
        )
        '''
        self.connection.execute(query)
        self.connection.commit()

    def add_student(self, roll_no, name, marks, attendance):
        """Add a new student"""
        if self.search_student(roll_no) is not None:
            return False, "Student with this roll number already exists!"

        query = '''INSERT INTO students (roll_no, name, marks, attendance)
                   VALUES (?, ?, ?, ?)'''
        try:
            self.connection.execute(query, (roll_no, name, marks, attendance))
            self.connection.commit()
            return True, "Student added successfully!"
        except sqlite3.DatabaseError as exc:
            return False, f"Database error: {exc}"

    def search_student(self, roll_no):
        """Search for a student by roll number"""
        query = 'SELECT * FROM students WHERE roll_no = ?'
        cursor = self.connection.execute(query, (roll_no,))
        row = cursor.fetchone()
        return Student(**row) if row else None

    def search_by_name(self, name):
        """Search for students by name"""
        query = 'SELECT * FROM students WHERE LOWER(name) LIKE ?'
        cursor = self.connection.execute(query, (f'%{name.lower()}%',))
        return [Student(**row) for row in cursor.fetchall()]

    def update_student(self, roll_no, name=None, marks=None, attendance=None):
        """Update student information"""
        student = self.search_student(roll_no)
        if student is None:
            return False, "Student not found!"

        new_name = name if name is not None else student.name
        new_marks = marks if marks is not None else student.marks
        new_attendance = attendance if attendance is not None else student.attendance

        query = '''UPDATE students SET name = ?, marks = ?, attendance = ?
                   WHERE roll_no = ?'''
        self.connection.execute(query, (new_name, new_marks, new_attendance, roll_no))
        self.connection.commit()
        return True, "Student updated successfully!"

    def delete_student(self, roll_no):
        """Delete a student"""
        if self.search_student(roll_no) is None:
            return False, "Student not found!"

        query = 'DELETE FROM students WHERE roll_no = ?'
        self.connection.execute(query, (roll_no,))
        self.connection.commit()
        return True, "Student deleted successfully!"

    def get_all_students(self):
        """Get all students"""
        query = 'SELECT * FROM students ORDER BY roll_no'
        cursor = self.connection.execute(query)
        return [Student(**row) for row in cursor.fetchall()]

    def get_total_students(self):
        """Get total number of students"""
        query = 'SELECT COUNT(*) AS total FROM students'
        cursor = self.connection.execute(query)
        row = cursor.fetchone()
        return row['total'] if row else 0

    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
