class Student:
    """Class to manage student information"""
    
    def __init__(self, roll_no, name, marks, attendance):
        """Initialize a student object"""
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.attendance = attendance
    
    def update(self, name=None, marks=None, attendance=None):
        """Update student information"""
        if name is not None:
            self.name = name
        if marks is not None:
            self.marks = marks
        if attendance is not None:
            self.attendance = attendance
    
    def to_dict(self):
        """Convert student to dictionary"""
        return {
            'roll_no': self.roll_no,
            'name': self.name,
            'marks': self.marks,
            'attendance': self.attendance
        }
    
    def __str__(self):
        """String representation of student"""
        return f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}, Attendance: {self.attendance}%"
