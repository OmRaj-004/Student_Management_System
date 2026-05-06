import tkinter as tk
from tkinter import messagebox, ttk
from database import StudentDatabase
from reports import ReportGenerator

class StudentManagementGUI:
    """Tkinter GUI for the Student Management System"""

    def __init__(self, db_filename='students.db'):
        self.db = StudentDatabase(filename=db_filename)
        self.report_generator = ReportGenerator(self.db)
        self.root = tk.Tk()
        self.root.title("Student Management System")
        self.root.geometry("960x620")
        self.root.resizable(False, False)

        self._setup_styles()
        self._build_widgets()
        self._refresh_student_table()

    def _setup_styles(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure('TButton', font=('Segoe UI', 10), padding=6)
        style.configure('TLabel', font=('Segoe UI', 10))
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'))
        style.configure('Treeview', font=('Segoe UI', 10), rowheight=28)
        style.configure('Treeview.Heading', font=('Segoe UI', 10, 'bold'))

    def _build_widgets(self):
        title = ttk.Label(self.root, text="Student Management System", style='Header.TLabel')
        title.pack(pady=10)

        form_frame = ttk.Frame(self.root)
        form_frame.pack(fill='x', padx=16)

        ttk.Label(form_frame, text="Roll Number:").grid(row=0, column=0, sticky='w', padx=4, pady=4)
        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky='w', padx=4, pady=4)
        ttk.Label(form_frame, text="Marks:").grid(row=0, column=2, sticky='w', padx=4, pady=4)
        ttk.Label(form_frame, text="Attendance (%):").grid(row=1, column=2, sticky='w', padx=4, pady=4)

        self.roll_entry = ttk.Entry(form_frame, width=24)
        self.name_entry = ttk.Entry(form_frame, width=24)
        self.marks_entry = ttk.Entry(form_frame, width=24)
        self.attendance_entry = ttk.Entry(form_frame, width=24)

        self.roll_entry.grid(row=0, column=1, padx=4, pady=4)
        self.name_entry.grid(row=1, column=1, padx=4, pady=4)
        self.marks_entry.grid(row=0, column=3, padx=4, pady=4)
        self.attendance_entry.grid(row=1, column=3, padx=4, pady=4)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill='x', padx=16, pady=8)

        ttk.Button(button_frame, text="Add Student", command=self.add_student).grid(row=0, column=0, padx=4)
        ttk.Button(button_frame, text="Update Student", command=self.update_student).grid(row=0, column=1, padx=4)
        ttk.Button(button_frame, text="Delete Student", command=self.delete_student).grid(row=0, column=2, padx=4)
        ttk.Button(button_frame, text="Clear Fields", command=self.clear_fields).grid(row=0, column=3, padx=4)

        search_frame = ttk.LabelFrame(self.root, text="Search")
        search_frame.pack(fill='x', padx=16, pady=8)

        ttk.Label(search_frame, text="Search by:").grid(row=0, column=0, sticky='w', padx=4, pady=4)
        self.search_option = ttk.Combobox(search_frame, values=["Roll Number", "Name"], state='readonly', width=16)
        self.search_option.current(0)
        self.search_option.grid(row=0, column=1, padx=4, pady=4)

        ttk.Label(search_frame, text="Search text:").grid(row=0, column=2, sticky='w', padx=4, pady=4)
        self.search_entry = ttk.Entry(search_frame, width=24)
        self.search_entry.grid(row=0, column=3, padx=4, pady=4)

        ttk.Button(search_frame, text="Search", command=self.search_student).grid(row=0, column=4, padx=4)
        ttk.Button(search_frame, text="View All", command=self._refresh_student_table).grid(row=0, column=5, padx=4)

        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(fill='both', expand=True, padx=16, pady=8)

        columns = ('roll_no', 'name', 'marks', 'attendance')
        self.student_table = ttk.Treeview(self.tree_frame, columns=columns, show='headings', selectmode='browse')
        self.student_table.heading('roll_no', text='Roll Number')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('marks', text='Marks')
        self.student_table.heading('attendance', text='Attendance (%)')
        self.student_table.column('roll_no', width=140, anchor='center')
        self.student_table.column('name', width=320, anchor='w')
        self.student_table.column('marks', width=120, anchor='center')
        self.student_table.column('attendance', width=140, anchor='center')
        self.student_table.pack(fill='both', expand=True, side='left')
        self.student_table.bind('<<TreeviewSelect>>', self.on_row_select)

        scrollbar = ttk.Scrollbar(self.tree_frame, orient='vertical', command=self.student_table.yview)
        scrollbar.pack(side='right', fill='y')
        self.student_table.configure(yscroll=scrollbar.set)

        report_frame = ttk.LabelFrame(self.root, text="Reports")
        report_frame.pack(fill='x', padx=16, pady=8)

        ttk.Button(report_frame, text="Class Report", command=lambda: self.show_report('class')).grid(row=0, column=0, padx=4, pady=4)
        ttk.Button(report_frame, text="Top Performers", command=lambda: self.show_report('toppers')).grid(row=0, column=1, padx=4, pady=4)
        ttk.Button(report_frame, text="Attendance Report", command=lambda: self.show_report('attendance')).grid(row=0, column=2, padx=4, pady=4)
        ttk.Button(report_frame, text="Marks Distribution", command=lambda: self.show_report('marks_distribution')).grid(row=0, column=3, padx=4, pady=4)

        self.status_label = ttk.Label(self.root, text="Ready", style='TLabel')
        self.status_label.pack(fill='x', padx=16, pady=6)

    def add_student(self):
        roll_no = self.roll_entry.get().strip()
        name = self.name_entry.get().strip()
        marks = self.marks_entry.get().strip()
        attendance = self.attendance_entry.get().strip()

        if not roll_no or not name or not marks or not attendance:
            self._set_status('All fields are required.', error=True)
            return

        try:
            marks = float(marks)
            attendance = float(attendance)
        except ValueError:
            self._set_status('Marks and attendance must be valid numbers.', error=True)
            return

        if not 0 <= marks <= 100 or not 0 <= attendance <= 100:
            self._set_status('Marks and attendance must be between 0 and 100.', error=True)
            return

        success, message = self.db.add_student(roll_no, name, marks, attendance)
        self._set_status(message, error=not success)
        if success:
            self._refresh_student_table()
            self.clear_fields()

    def search_student(self):
        search_term = self.search_entry.get().strip()
        if not search_term:
            self._set_status('Enter text to search.', error=True)
            return

        option = self.search_option.get()
        students = []
        if option == 'Roll Number':
            student = self.db.search_student(search_term)
            if student:
                students = [student]
        else:
            students = self.db.search_by_name(search_term)

        if not students:
            self._set_status('No matching students found.', error=True)
        else:
            self._set_status(f'Found {len(students)} matching record(s).')
        self._populate_student_table(students)

    def update_student(self):
        selected = self.student_table.selection()
        if not selected:
            self._set_status('Select a student row to update.', error=True)
            return

        roll_no = self.roll_entry.get().strip()
        name = self.name_entry.get().strip() or None
        marks = self.marks_entry.get().strip()
        attendance = self.attendance_entry.get().strip()

        if not roll_no:
            self._set_status('Roll number is required to update.', error=True)
            return

        try:
            marks = float(marks) if marks else None
            attendance = float(attendance) if attendance else None
        except ValueError:
            self._set_status('Marks and attendance must be valid numbers.', error=True)
            return

        success, message = self.db.update_student(roll_no, name=name, marks=marks, attendance=attendance)
        self._set_status(message, error=not success)
        if success:
            self._refresh_student_table()
            self.clear_fields()

    def delete_student(self):
        selected = self.student_table.selection()
        if not selected:
            self._set_status('Select a student row to delete.', error=True)
            return

        roll_no = self.student_table.set(selected[0], 'roll_no')
        confirmed = messagebox.askyesno('Delete Student', f'Are you sure you want to delete {roll_no}?')
        if not confirmed:
            return

        success, message = self.db.delete_student(roll_no)
        self._set_status(message, error=not success)
        if success:
            self._refresh_student_table()
            self.clear_fields()

    def clear_fields(self):
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
        self.attendance_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.student_table.selection_remove(self.student_table.selection())
        self._set_status('Ready')

    def _refresh_student_table(self):
        students = self.db.get_all_students()
        self._populate_student_table(students)
        self._set_status(f'{len(students)} student(s) loaded.')

    def _populate_student_table(self, students):
        for row in self.student_table.get_children():
            self.student_table.delete(row)

        for student in students:
            self.student_table.insert('', tk.END, values=(student.roll_no, student.name, student.marks, student.attendance))

    def on_row_select(self, event):
        selected = self.student_table.selection()
        if not selected:
            return
        values = self.student_table.item(selected[0], 'values')
        self.roll_entry.delete(0, tk.END)
        self.roll_entry.insert(0, values[0])
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[1])
        self.marks_entry.delete(0, tk.END)
        self.marks_entry.insert(0, values[2])
        self.attendance_entry.delete(0, tk.END)
        self.attendance_entry.insert(0, values[3])
        self._set_status(f'Selected student {values[0]}')

    def show_report(self, report_key):
        mapping = {
            'class': ('Class Report', self.report_generator.generate_class_report),
            'toppers': ('Top Performers Report', self.report_generator.generate_toppers_report),
            'attendance': ('Attendance Report', self.report_generator.generate_attendance_report),
            'marks_distribution': ('Marks Distribution Report', self.report_generator.generate_marks_report)
        }
        title, generator = mapping[report_key]
        content = generator()
        self._open_report_window(title, content)

    def _open_report_window(self, title, report_text):
        report_window = tk.Toplevel(self.root)
        report_window.title(title)
        report_window.geometry('760x520')

        text_widget = tk.Text(report_window, wrap='word', font=('Segoe UI', 10))
        text_widget.insert('1.0', report_text)
        text_widget.configure(state='disabled')
        text_widget.pack(fill='both', expand=True, padx=8, pady=8)

        button_frame = ttk.Frame(report_window)
        button_frame.pack(fill='x', padx=8, pady=8)
        ttk.Button(button_frame, text='Save Report', command=lambda: self._save_report(report_text)).pack(side='left')
        ttk.Button(button_frame, text='Close', command=report_window.destroy).pack(side='right')

    def _save_report(self, report_text):
        filename = 'student_report.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(report_text)
            messagebox.showinfo('Save Report', f'Report saved to {filename}')
        except IOError as exc:
            messagebox.showerror('Save Report', f'Unable to save report: {exc}')

    def _set_status(self, message, error=False):
        self.status_label.config(text=message)
        self.status_label.configure(foreground='red' if error else 'green')

    def run(self):
        self.root.protocol('WM_DELETE_WINDOW', self._on_close)
        self.root.mainloop()

    def _on_close(self):
        self.db.close()
        self.root.destroy()
