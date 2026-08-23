import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from database import (
    add_student, add_marks, get_all_students, get_student,
    search_students, get_student_exams, get_exam,
    update_exam, delete_exam, delete_student
)

from analysis import (
    exam_percentage, calculate_subject_averages,
    calculate_student_average, find_strongest_weakest_subject,
    compare_exams, classify_performance,
    calculate_student_rankings, calculate_class_statistics
)

from reports import export_student_report

from visualization import (
    show_subject_averages,
    show_exam_progress,
    show_exam_comparison
)


class MarksAnalyserGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Marks Analyser V5")
        self.root.geometry("1050x650")
        self.build()
        self.refresh_students()

    # ---------- MAIN UI ----------

    def build(self):
        ttk.Label(
            self.root,
            text="MARKS ANALYSER V5",
            font=("Arial", 24, "bold")
        ).pack(pady=(15, 2))

        ttk.Label(
            self.root,
            text="Student Performance Management System"
        ).pack(pady=(0, 12))

        main = ttk.Frame(self.root, padding=10)
        main.pack(fill="both", expand=True)

        left = ttk.LabelFrame(main, text="Students", padding=10)
        left.pack(side="left", fill="y", padx=(0, 10))

        self.search = ttk.Entry(left)
        self.search.pack(fill="x", pady=5)
        self.search.bind("<KeyRelease>", self.search_students)

        self.students = tk.Listbox(left, width=28, height=22)
        self.students.pack(fill="both", expand=True)
        self.students.bind("<<ListboxSelect>>", self.select_student)

        ttk.Button(
            left, text="Add Student",
            command=self.add_student
        ).pack(fill="x", pady=5)

        ttk.Button(
            left, text="Delete Student",
            command=self.delete_student
        ).pack(fill="x")

        right = ttk.Frame(main)
        right.pack(side="right", fill="both", expand=True)

        self.title = ttk.Label(
            right,
            text="Select a student",
            font=("Arial", 18, "bold")
        )
        self.title.pack(anchor="w", pady=5)

        self.tabs = ttk.Notebook(right)
        self.tabs.pack(fill="both", expand=True)

        self.dashboard = self.text_tab("Dashboard")
        self.exams_tab()
        self.analysis = self.text_tab("Analysis")
        self.actions_tab()

    def text_tab(self, name):
        frame = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(frame, text=name)

        text = tk.Text(
            frame,
            font=("Consolas", 10),
            state="disabled"
        )
        text.pack(fill="both", expand=True)
        return text

    # ---------- EXAMS ----------

    def exams_tab(self):
        frame = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(frame, text="Exam History")

        columns = (
            "id", "exam", "physics", "chemistry",
            "biology", "total", "percentage"
        )

        self.exam_tree = ttk.Treeview(
            frame, columns=columns, show="headings"
        )

        headings = [
            "ID", "Exam", "Physics", "Chemistry",
            "Biology", "Total", "%"
        ]

        for column, heading in zip(columns, headings):
            self.exam_tree.heading(column, text=heading)
            self.exam_tree.column(column, width=90)

        self.exam_tree.pack(fill="both", expand=True)

    # ---------- ACTIONS ----------

    def actions_tab(self):
        frame = ttk.Frame(self.tabs, padding=15)
        self.tabs.add(frame, text="Actions")

        actions = [
            ("Add Exam", self.add_exam),
            ("Update Exam", self.update_exam),
            ("Delete Exam", self.delete_exam),
            ("Compare Exams", self.compare),
            ("Export Report", self.export_report),
            ("Subject Averages", self.subject_graph),
            ("Exam Progress", self.progress_graph),
            ("Class Rankings", self.rankings)
        ]

        for text, command in actions:
            ttk.Button(
                frame,
                text=text,
                command=command
            ).pack(fill="x", pady=4)

    # ---------- STUDENTS ----------

    def refresh_students(self):
        self.students.delete(0, tk.END)

        for student in get_all_students():
            self.students.insert(
                tk.END,
                f"{student[0]} | {student[1]}"
            )

    def search_students(self, event=None):
        text = self.search.get().strip()

        if not text:
            self.refresh_students()
            return

        self.students.delete(0, tk.END)

        for student in search_students(text):
            self.students.insert(
                tk.END,
                f"{student[0]} | {student[1]}"
            )

    def selected_student(self):
        selection = self.students.curselection()

        if not selection:
            return None

        student_id = int(
            self.students.get(selection[0]).split("|")[0]
        )

        return get_student(student_id)

    def select_student(self, event=None):
        student = self.selected_student()

        if student:
            self.title.config(
                text=f"Student: {student[1]}"
            )
            self.load_student(student)

    def add_student(self):
        self.popup(
            "Add Student",
            [("Name", "")],
            lambda values: self.save_student(values[0])
        )

    def save_student(self, name):
        name = name.strip()

        if not name:
            messagebox.showerror(
                "Error",
                "Student name cannot be empty."
            )
            return

        student_id = add_student(name)

        messagebox.showinfo(
            "Success",
            f"Student added.\nID: {student_id}"
        )

        self.refresh_students()

    def delete_student(self):
        student = self.selected_student()

        if not student:
            messagebox.showwarning(
                "Select Student",
                "Please select a student."
            )
            return

        if messagebox.askyesno(
            "Confirm",
            f"Delete {student[1]} and all exams?"
        ):
            delete_student(student[0])
            self.refresh_students()
            self.clear_data()

    # ---------- LOAD DATA ----------

    def load_student(self, student):
        exams = get_student_exams(student[0])

        self.load_exams(exams)
        self.load_dashboard(student, exams)
        self.load_analysis(exams)

    def load_exams(self, exams):
        for item in self.exam_tree.get_children():
            self.exam_tree.delete(item)

        for exam in exams:
            total = exam[6] + exam[7] + exam[8]
            maximum = exam[3] + exam[4] + exam[5]

            self.exam_tree.insert(
                "",
                tk.END,
                values=(
                    exam[0],
                    exam[2],
                    f"{exam[6]}/{exam[3]}",
                    f"{exam[7]}/{exam[4]}",
                    f"{exam[8]}/{exam[5]}",
                    f"{total}/{maximum}",
                    f"{exam_percentage(exam):.2f}%"
                )
            )

    def load_dashboard(self, student, exams):
        if not exams:
            self.set_text(
                self.dashboard,
                "No exam data available."
            )
            return

        average = calculate_student_average(exams)
        strongest, weakest = find_strongest_weakest_subject(exams)

        best = max(exams, key=exam_percentage)
        worst = min(exams, key=exam_percentage)

        text = (
            f"STUDENT DASHBOARD\n"
            f"{'=' * 35}\n\n"
            f"Student : {student[1]}\n"
            f"ID      : {student[0]}\n"
            f"Exams   : {len(exams)}\n\n"
            f"Average : {average:.2f}%\n"
            f"Level   : {classify_performance(average)}\n\n"
            f"Strongest Subject : {strongest}\n"
            f"Weakest Subject   : {weakest}\n\n"
            f"Best Exam  : {best[2]} "
            f"({exam_percentage(best):.2f}%)\n"
            f"Worst Exam : {worst[2]} "
            f"({exam_percentage(worst):.2f}%)"
        )

        self.set_text(self.dashboard, text)

    def load_analysis(self, exams):
        if not exams:
            self.set_text(
                self.analysis,
                "No exam data available."
            )
            return

        p, c, b = calculate_subject_averages(exams)
        percentages = [exam_percentage(e) for e in exams]

        text = (
            f"PERFORMANCE ANALYSIS\n"
            f"{'=' * 35}\n\n"
            f"Overall Average : "
            f"{calculate_student_average(exams):.2f}%\n"
            f"Highest Exam    : {max(percentages):.2f}%\n"
            f"Lowest Exam     : {min(percentages):.2f}%\n\n"
            f"Physics Average   : {p:.2f}%\n"
            f"Chemistry Average : {c:.2f}%\n"
            f"Biology Average   : {b:.2f}%"
        )

        if len(exams) >= 2:
            change = percentages[-1] - percentages[0]
            text += (
                f"\n\nOverall Change : "
                f"{change:+.2f} percentage points"
            )

        self.set_text(self.analysis, text)

    # ---------- EXAMS ----------

    def selected_exam(self):
        selection = self.exam_tree.selection()

        if not selection:
            messagebox.showwarning(
                "Select Exam",
                "Please select an exam."
            )
            return None

        exam_id = int(
            self.exam_tree.item(selection[0])["values"][0]
        )

        return get_exam(exam_id)

    def add_exam(self):
        student = self.selected_student()

        if not student:
            messagebox.showwarning(
                "Select Student",
                "Please select a student first."
            )
            return

        self.exam_form(student)

    def exam_form(self, student, exam=None):
        fields = [
            ("Exam Name", exam[2] if exam else ""),
            ("Physics Maximum", exam[3] if exam else ""),
            ("Chemistry Maximum", exam[4] if exam else ""),
            ("Biology Maximum", exam[5] if exam else ""),
            ("Physics Marks", exam[6] if exam else ""),
            ("Chemistry Marks", exam[7] if exam else ""),
            ("Biology Marks", exam[8] if exam else "")
        ]

        def save(values):
            try:
                name = values[0].strip()
                maximums = list(map(float, values[1:4]))
                marks = list(map(float, values[4:7]))

                if not name:
                    raise ValueError("Exam name is required.")

                if any(x <= 0 for x in maximums):
                    raise ValueError(
                        "Maximum marks must be greater than 0."
                    )

                if any(
                    mark < 0 or mark > maximum
                    for mark, maximum in zip(marks, maximums)
                ):
                    raise ValueError(
                        "Marks must be between 0 and maximum."
                    )

                if exam:
                    update_exam(
                        exam[0], name,
                        *maximums, *marks
                    )
                else:
                    add_marks(
                        student[0], name,
                        *maximums, *marks
                    )

                window.destroy()
                self.load_student(student)

            except ValueError as error:
                messagebox.showerror(
                    "Invalid Input",
                    str(error)
                )

        window = self.popup(
            "Update Exam" if exam else "Add Exam",
            fields,
            save,
            return_window=True
        )

    def update_exam(self):
        student = self.selected_student()
        exam = self.selected_exam()

        if student and exam:
            self.exam_form(student, exam)

    def delete_exam(self):
        student = self.selected_student()
        exam = self.selected_exam()

        if not student or not exam:
            return

        if messagebox.askyesno(
            "Confirm",
            f"Delete '{exam[2]}'?"
        ):
            delete_exam(exam[0])
            self.load_student(student)

    # ---------- COMPARISON ----------

    def compare(self):
        student = self.selected_student()

        if not student:
            return

        exams = get_student_exams(student[0])

        if len(exams) < 2:
            messagebox.showwarning(
                "Not Enough Data",
                "At least two exams are required."
            )
            return

        self.compare_window(exams)

    def compare_window(self, exams):
        window = tk.Toplevel(self.root)
        window.title("Compare Exams")
        window.geometry("350x250")

        values = [
            f"{exam[0]} | {exam[2]}"
            for exam in exams
        ]

        ttk.Label(window, text="First Exam").pack(pady=5)
        first = ttk.Combobox(
            window, values=values, state="readonly"
        )
        first.pack()

        ttk.Label(window, text="Second Exam").pack(pady=5)
        second = ttk.Combobox(
            window, values=values, state="readonly"
        )
        second.pack()

        def run():
            if not first.get() or not second.get():
                return

            a = get_exam(int(first.get().split("|")[0]))
            b = get_exam(int(second.get().split("|")[0]))

            if a[0] == b[0]:
                messagebox.showerror(
                    "Error",
                    "Choose two different exams."
                )
                return

            p1, p2, change = compare_exams(a, b)

            messagebox.showinfo(
                "Comparison",
                f"{a[2]}: {p1:.2f}%\n"
                f"{b[2]}: {p2:.2f}%\n\n"
                f"Change: {change:+.2f} points"
            )

        ttk.Button(
            window,
            text="Compare",
            command=run
        ).pack(pady=20)

    # ---------- REPORT ----------

    def export_report(self):
        student = self.selected_student()

        if not student:
            return

        exams = get_student_exams(student[0])

        if not exams:
            messagebox.showwarning(
                "No Data",
                "No exams available."
            )
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )

        if filename and export_student_report(
            student, exams, filename
        ):
            messagebox.showinfo(
                "Success",
                "Report exported successfully."
            )

    # ---------- GRAPHS ----------

    def subject_graph(self):
        student = self.selected_student()

        if student:
            exams = get_student_exams(student[0])
            show_subject_averages(exams)

    def progress_graph(self):
        student = self.selected_student()

        if student:
            exams = get_student_exams(student[0])
            show_exam_progress(exams)

    # ---------- RANKINGS ----------

    def rankings(self):
        data = []

        for student in get_all_students():
            data.append(
                (student, get_student_exams(student[0]))
            )

        rankings = calculate_student_rankings(data)

        if not rankings:
            messagebox.showinfo(
                "Rankings",
                "No exam data available."
            )
            return

        stats = calculate_class_statistics(rankings)

        text = "CLASS RANKINGS\n" + "=" * 40 + "\n\n"

        for student in rankings:
            text += (
                f"{student['rank']}. "
                f"{student['name']} - "
                f"{student['average']:.2f}% "
                f"({student['classification']})\n"
            )

        text += (
            f"\nClass Average : "
            f"{stats['class_average']:.2f}%\n"
            f"Highest       : "
            f"{stats['highest']:.2f}%\n"
            f"Lowest        : "
            f"{stats['lowest']:.2f}%"
        )

        messagebox.showinfo(
            "Class Rankings",
            text
        )

    # ---------- HELPERS ----------

    def set_text(self, widget, text):
        widget.config(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, text)
        widget.config(state="disabled")

    def clear_data(self):
        self.title.config(text="Select a student")
        self.set_text(self.dashboard, "Select a student.")
        self.set_text(self.analysis, "Select a student.")

        for item in self.exam_tree.get_children():
            self.exam_tree.delete(item)

    def popup(
        self,
        title,
        fields,
        save_function,
        return_window=False
    ):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.resizable(False, False)

        entries = []

        frame = ttk.Frame(window, padding=15)
        frame.pack()

        for row, (label, value) in enumerate(fields):
            ttk.Label(
                frame,
                text=label
            ).grid(row=row, column=0, sticky="w", pady=5)

            entry = ttk.Entry(frame, width=25)
            entry.insert(0, str(value))
            entry.grid(row=row, column=1, padx=10, pady=5)

            entries.append(entry)

        def save():
            save_function([entry.get() for entry in entries])

        ttk.Button(
            frame,
            text="Save",
            command=save
        ).grid(
            row=len(fields),
            column=0,
            columnspan=2,
            pady=10
        )

        if return_window:
            return window


def start_gui():
    root = tk.Tk()
    MarksAnalyserGUI(root)
    root.mainloop()