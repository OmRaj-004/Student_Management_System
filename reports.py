class ReportGenerator:
    """Generate reports from student data"""
    
    def __init__(self, database):
        self.db = database
    
    def generate_class_report(self):
        """Generate a comprehensive class report"""
        students = self.db.get_all_students()
        if not students:
            return "No students in the system!"
        
        report = "\n" + "="*60
        report += "\nCLASS REPORT"
        report += "\n" + "="*60 + "\n"
        
        for student in students:
            report += f"{student}\n"
        
        report += "\n" + "-"*60 + "\n"
        report += f"Total Students: {len(students)}\n"
        
        avg_marks = sum(s.marks for s in students) / len(students)
        avg_attendance = sum(s.attendance for s in students) / len(students)
        
        report += f"Average Marks: {avg_marks:.2f}\n"
        report += f"Average Attendance: {avg_attendance:.2f}%\n"
        
        report += "-"*60 + "\n"
        return report
    
    def generate_toppers_report(self, top_count=5):
        """Generate report of top performers"""
        students = sorted(self.db.get_all_students(), key=lambda x: x.marks, reverse=True)
        
        if not students:
            return "No students in the system!"
        
        report = "\n" + "="*60
        report += "\nTOP PERFORMERS REPORT"
        report += "\n" + "="*60 + "\n"
        
        top_students = students[:min(top_count, len(students))]
        for i, student in enumerate(top_students, 1):
            report += f"{i}. {student}\n"
        
        report += "="*60 + "\n"
        return report
    
    def generate_attendance_report(self, min_attendance=75):
        """Generate attendance report"""
        students = self.db.get_all_students()
        
        if not students:
            return "No students in the system!"
        
        good_attendance = [s for s in students if s.attendance >= min_attendance]
        poor_attendance = [s for s in students if s.attendance < min_attendance]
        
        report = "\n" + "="*60
        report += "\nATTENDANCE REPORT"
        report += "\n" + "="*60 + "\n"
        
        report += f"\nGood Attendance (>= {min_attendance}%): {len(good_attendance)}\n"
        report += "-"*60 + "\n"
        for student in good_attendance:
            report += f"{student.name} ({student.roll_no}): {student.attendance}%\n"
        
        report += f"\nPoor Attendance (< {min_attendance}%): {len(poor_attendance)}\n"
        report += "-"*60 + "\n"
        for student in poor_attendance:
            report += f"{student.name} ({student.roll_no}): {student.attendance}%\n"
        
        report += "="*60 + "\n"
        return report
    
    def generate_marks_report(self):
        """Generate marks distribution report"""
        students = self.db.get_all_students()
        
        if not students:
            return "No students in the system!"
        
        grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        
        for student in students:
            if student.marks >= 90:
                grades['A'] += 1
            elif student.marks >= 80:
                grades['B'] += 1
            elif student.marks >= 70:
                grades['C'] += 1
            elif student.marks >= 60:
                grades['D'] += 1
            else:
                grades['F'] += 1
        
        report = "\n" + "="*60
        report += "\nMARKS DISTRIBUTION REPORT"
        report += "\n" + "="*60 + "\n"
        
        report += "Grade A (>= 90): " + str(grades['A']) + " students\n"
        report += "Grade B (80-89): " + str(grades['B']) + " students\n"
        report += "Grade C (70-79): " + str(grades['C']) + " students\n"
        report += "Grade D (60-69): " + str(grades['D']) + " students\n"
        report += "Grade F (< 60): " + str(grades['F']) + " students\n"
        report += "="*60 + "\n"
        
        return report
    
    def export_report_to_file(self, report_name, report_content):
        """Export report to a text file"""
        filename = f"{report_name}_report.txt"
        with open(filename, 'w') as f:
            f.write(report_content)
        return f"Report saved to {filename}"
