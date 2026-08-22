import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from database import (
    add_student,
    add_marks,
    get_all_students,
    get_student,
    search_students,
    get_student_exams,
    get_exam,
    update_exam,
    delete_exam,
    delete_student
)

from analysis import (
    exam_percentage,
    generate_performance_summary,
    compare_exams,
    calculate_student_rankings,
    calculate_class_statistics
)

from reports import export_student_report

from visualization import (
    show_student_performance_graph,
    show_subject_comparison,
    show_ranking_graph,
    show_subject_trends
)


# ============================================================
# MAIN GUI
# ============================================================

class MarksAnalyserGUI:

    def __init__(self, root):
        self.root = root

        self.root.title("Marks Analyser V5")
        self.root.geometry("1100x700")
        self.root.minsize(950, 600)

        self.create_style()
        self.create_layout()

        self.refresh_students()

    # ========================================================
    # STYLE
    # ========================================================

    def create_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Arial", 24, "bold")
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Arial", 11)
        )

        style.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        style.configure(
            "Action.TButton",
            font=("Arial", 10, "bold"),
            padding=8
        )

    # ========================================================
    # LAYOUT
    # ========================================================

    def create_layout(self):

        # ---------------- HEADER ----------------

        header = ttk.Frame(self.root, padding=15)
        header.pack(fill="x")

        ttk.Label(
            header,
            text="MARKS ANALYSER V5",
            style="Title.TLabel"
        ).pack()

        ttk.Label(
            header,
            text="Student Performance Management System",
            style="Subtitle.TLabel"
        ).pack(pady=(3, 0))

        # ---------------- MAIN FRAME ----------------

        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill="both", expand=True)

        # ---------------- LEFT PANEL ----------------

        left_frame = ttk.LabelFrame(
            main_frame,
            text="Students",
            padding=10
        )

        left_frame.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )

        # Search

        ttk.Label(
            left_frame,
            text="Search Student"
        ).pack(anchor="w")

        self.search_entry = ttk.Entry(
            left_frame,
            width=28
        )

        self.search_entry.pack(
            fill="x",
            pady=(5, 8)
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_student_live
        )

        # Student list

        student_frame = ttk.Frame(left_frame)
        student_frame.pack(
            fill="both",
            expand=True
        )

        self.student_list = tk.Listbox(
            student_frame,
            width=30,
            height=20,
            font=("Arial", 10)
        )

        self.student_list.pack(
            side="left",
            fill="both",
            expand=True
        )

        student_scroll = ttk.Scrollbar(
            student_frame,
            orient="vertical",
            command=self.student_list.yview
        )

        student_scroll.pack(
            side="right",
            fill="y"
        )

        self.student_list.config(
            yscrollcommand=student_scroll.set
        )

        self.student_list.bind(
            "<<ListboxSelect>>",
            self.student_selected
        )

        # Buttons

        ttk.Button(
            left_frame,
            text="Add Student",
            style="Action.TButton",
            command=self.add_student_window
        ).pack(
            fill="x",
            pady=(10, 5)
        )

        ttk.Button(
            left_frame,
            text="Delete Student",
            command=self.delete_selected_student
        ).pack(
            fill="x"
        )

        # ---------------- RIGHT PANEL ----------------

        right_frame = ttk.Frame(main_frame)
        right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Student title

        self.student_title = ttk.Label(
            right_frame,
            text="Select a student",
            font=("Arial", 18, "bold")
        )

        self.student_title.pack(
            anchor="w",
            pady=(0, 10)
        )

        # Notebook

        self.notebook = ttk.Notebook(
            right_frame
        )

        self.notebook.pack(
            fill="both",
            expand=True
        )

        self.create_dashboard_tab()
        self.create_exams_tab()
        self.create_analysis_tab()
        self.create_actions_tab()

    # ========================================================
    # DASHBOARD
    # ========================================================

    def create_dashboard_tab(self):

        self.dashboard_tab = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            self.dashboard_tab,
            text="Dashboard"
        )

        self.dashboard_text = tk.Text(
            self.dashboard_tab,
            wrap="word",
            font=("Consolas", 11),
            state="disabled"
        )

        self.dashboard_text.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # EXAMS TAB
    # ========================================================

    def create_exams_tab(self):

        self.exams_tab = ttk.Frame(
            self.notebook,
            padding=10
        )

        self.notebook.add(
            self.exams_tab,
            text="Exam History"
        )

        columns = (
            "id",
            "exam",
            "physics",
            "chemistry",
            "biology",
            "total",
            "percentage"
        )

        self.exam_tree = ttk.Treeview(
            self.exams_tab,
            columns=columns,
            show="headings"
        )

        headings = {
            "id": "ID",
            "exam": "Exam",
            "physics": "Physics",
            "chemistry": "Chemistry",
            "biology": "Biology",
            "total": "Total",
            "percentage": "%"
        }

        for column in columns:

            self.exam_tree.heading(
                column,
                text=headings[column]
            )

            self.exam_tree.column(
                column,
                width=100
            )

        self.exam_tree.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # ANALYSIS TAB
    # ========================================================

    def create_analysis_tab(self):

        self.analysis_tab = ttk.Frame(
            self.notebook,
            padding=10
        )

        self.notebook.add(
            self.analysis_tab,
            text="Analysis"
        )

        self.analysis_text = tk.Text(
            self.analysis_tab,
            wrap="word",
            font=("Consolas", 11),
            state="disabled"
        )

        self.analysis_text.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # ACTIONS TAB
    # ========================================================

    def create_actions_tab(self):

        self.actions_tab = ttk.Frame(
            self.notebook,
            padding=20
        )

        self.notebook.add(
            self.actions_tab,
            text="Actions"
        )

        buttons = [
            (
                "Add Exam",
                self.add_exam_window
            ),
            (
                "Update Exam",
                self.update_exam_window
            ),
            (
                "Delete Exam",
                self.delete_selected_exam
            ),
            (
                "Compare Exams",
                self.compare_selected_exams
            ),
            (
                "Export Report",
                self.export_report
            ),
            (
                "Performance Graph",
                self.performance_graph
            ),
            (
                "Subject Comparison",
                self.subject_graph
            ),
            (
                "Subject Trends",
                self.trend_graph
            ),
        ]

        for text, command in buttons:

            ttk.Button(
                self.actions_tab,
                text=text,
                style="Action.TButton",
                command=command
            ).pack(
                fill="x",
                pady=5
            )

        ttk.Separator(
            self.actions_tab
        ).pack(
            fill="x",
            pady=15
        )

        ttk.Button(
            self.actions_tab,
            text="Class Rankings",
            style="Action.TButton",
            command=self.show_rankings
        ).pack(
            fill="x",
            pady=5
        )

        ttk.Button(
            self.actions_tab,
            text="Ranking Graph",
            command=self.ranking_graph
        ).pack(
            fill="x",
            pady=5
        )

    # ========================================================
    # STUDENT FUNCTIONS
    # ========================================================

    def refresh_students(self):

        self.student_list.delete(
            0,
            tk.END
        )

        students = get_all_students()

        for student in students:

            self.student_list.insert(
                tk.END,
                f"{student[0]} | {student[1]}"
            )

    def search_student_live(self, event=None):

        search_term = self.search_entry.get().strip()

        if not search_term:

            self.refresh_students()
            return

        students = search_students(
            search_term
        )

        self.student_list.delete(
            0,
            tk.END
        )

        for student in students:

            self.student_list.insert(
                tk.END,
                f"{student[0]} | {student[1]}"
            )

    def get_selected_student(self):

        selection = self.student_list.curselection()

        if not selection:
            return None

        text = self.student_list.get(
            selection[0]
        )

        student_id = int(
            text.split("|")[0].strip()
        )

        return get_student(student_id)

    def student_selected(self, event=None):

        student = self.get_selected_student()

        if student is None:
            return

        self.student_title.config(
            text=f"Student: {student[1]}"
        )

        self.load_student_data(student)

    # ========================================================
    # LOAD STUDENT DATA
    # ========================================================

    def load_student_data(self, student):

        exams = get_student_exams(
            student[0]
        )

        self.load_exams(exams)
        self.load_dashboard(student, exams)
        self.load_analysis(exams)

    def load_exams(self, exams):

        for item in self.exam_tree.get_children():

            self.exam_tree.delete(item)

        for exam in exams:

            total = (
                exam[6]
                + exam[7]
                + exam[8]
            )

            maximum = (
                exam[3]
                + exam[4]
                + exam[5]
            )

            percentage = (
                total / maximum
            ) * 100

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
                    f"{percentage:.2f}%"
                )
            )

    # ========================================================
    # DASHBOARD / ANALYSIS TEXT
    # ========================================================

    def set_text(self, widget, text):

        widget.config(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        widget.insert(
            tk.END,
            text
        )

        widget.config(
            state="disabled"
        )

    def load_dashboard(
        self,
        student,
        exams
    ):

        if not exams:

            self.set_text(
                self.dashboard_text,
                "No exam data available."
            )

            return

        average = sum(
            exam_percentage(exam)
            for exam in exams
        ) / len(exams)

        best = max(
            exams,
            key=exam_percentage
        )

        worst = min(
            exams,
            key=exam_percentage
        )

        text = ""

        text += "========================================\n"
        text += "           STUDENT DASHBOARD\n"
        text += "========================================\n\n"

        text += f"Student: {student[1]}\n"
        text += f"Student ID: {student[0]}\n\n"

        text += f"Number of exams: {len(exams)}\n"
        text += f"Overall average: {average:.2f}%\n\n"

        text += (
            f"Best exam: {best[2]} "
            f"({exam_percentage(best):.2f}%)\n"
        )

        text += (
            f"Worst exam: {worst[2]} "
            f"({exam_percentage(worst):.2f}%)\n"
        )

        self.set_text(
            self.dashboard_text,
            text
        )

    def load_analysis(self, exams):

        if not exams:

            self.set_text(
                self.analysis_text,
                "No exam data available."
            )

            return

        text = ""

        average = sum(
            exam_percentage(exam)
            for exam in exams
        ) / len(exams)

        percentages = [
            exam_percentage(exam)
            for exam in exams
        ]

        highest = max(percentages)
        lowest = min(percentages)

        text += "========================================\n"
        text += "          PERFORMANCE ANALYSIS\n"
        text += "========================================\n\n"

        text += f"Overall average: {average:.2f}%\n"
        text += f"Highest exam: {highest:.2f}%\n"
        text += f"Lowest exam: {lowest:.2f}%\n"
        text += (
            f"Range: {highest - lowest:.2f} "
            "percentage points\n"
        )

        if len(exams) >= 2:

            change = (
                percentages[-1]
                - percentages[0]
            )

            text += (
                f"\nOverall change: "
                f"{change:+.2f} percentage points\n"
            )

        self.set_text(
            self.analysis_text,
            text
        )

    # ========================================================
    # ADD STUDENT
    # ========================================================

    def add_student_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Add Student"
        )

        window.geometry(
            "400x200"
        )

        window.transient(
            self.root
        )

        ttk.Label(
            window,
            text="Student Name"
        ).pack(
            pady=(25, 5)
        )

        name_entry = ttk.Entry(
            window,
            width=35
        )

        name_entry.pack()

        def save():

            name = name_entry.get().strip()

            if not name:

                messagebox.showerror(
                    "Error",
                    "Student name cannot be empty."
                )

                return

            student_id = add_student(
                name
            )

            messagebox.showinfo(
                "Success",
                f"Student added successfully.\n\n"
                f"Student ID: {student_id}"
            )

            window.destroy()

            self.refresh_students()

        ttk.Button(
            window,
            text="Save Student",
            command=save
        ).pack(
            pady=20
        )

    # ========================================================
    # ADD EXAM
    # ========================================================

    def add_exam_window(self):

        student = self.get_selected_student()

        if student is None:

            messagebox.showwarning(
                "No Student",
                "Please select a student first."
            )

            return

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Add Exam"
        )

        window.geometry(
            "450x500"
        )

        ttk.Label(
            window,
            text=f"Add Exam - {student[1]}",
            font=("Arial", 14, "bold")
        ).pack(
            pady=15
        )

        frame = ttk.Frame(
            window,
            padding=15
        )

        frame.pack(
            fill="both",
            expand=True
        )

        entries = {}

        fields = [
            "Exam Name",
            "Physics Maximum",
            "Chemistry Maximum",
            "Biology Maximum",
            "Physics Marks",
            "Chemistry Marks",
            "Biology Marks"
        ]

        for index, field in enumerate(fields):

            ttk.Label(
                frame,
                text=field
            ).grid(
                row=index,
                column=0,
                sticky="w",
                pady=7
            )

            entry = ttk.Entry(
                frame,
                width=25
            )

            entry.grid(
                row=index,
                column=1,
                pady=7,
                padx=10
            )

            entries[field] = entry

        def save():

            try:

                exam_name = (
                    entries["Exam Name"]
                    .get()
                    .strip()
                )

                if not exam_name:
                    raise ValueError(
                        "Exam name cannot be empty."
                    )

                physics_max = float(
                    entries["Physics Maximum"].get()
                )

                chemistry_max = float(
                    entries["Chemistry Maximum"].get()
                )

                biology_max = float(
                    entries["Biology Maximum"].get()
                )

                physics = float(
                    entries["Physics Marks"].get()
                )

                chemistry = float(
                    entries["Chemistry Marks"].get()
                )

                biology = float(
                    entries["Biology Marks"].get()
                )

                maximums = [
                    physics_max,
                    chemistry_max,
                    biology_max
                ]

                marks = [
                    physics,
                    chemistry,
                    biology
                ]

                for maximum in maximums:

                    if maximum <= 0:
                        raise ValueError(
                            "Maximum marks must be greater than 0."
                        )

                for mark, maximum in zip(
                    marks,
                    maximums
                ):

                    if mark < 0 or mark > maximum:

                        raise ValueError(
                            "Marks must be between "
                            "0 and the maximum marks."
                        )

                add_marks(
                    student[0],
                    exam_name,
                    physics_max,
                    chemistry_max,
                    biology_max,
                    physics,
                    chemistry,
                    biology
                )

                messagebox.showinfo(
                    "Success",
                    "Exam saved successfully."
                )

                window.destroy()

                self.load_student_data(
                    student
                )

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Input",
                    str(error)
                )

        ttk.Button(
            window,
            text="Save Exam",
            command=save
        ).pack(
            pady=15
        )

    # ========================================================
    # GET SELECTED EXAM
    # ========================================================

    def get_selected_exam_id(self):

        selection = self.exam_tree.selection()

        if not selection:

            messagebox.showwarning(
                "No Exam",
                "Please select an exam first."
            )

            return None

        values = self.exam_tree.item(
            selection[0]
        )["values"]

        return int(values[0])

    # ========================================================
    # UPDATE EXAM
    # ========================================================

    def update_exam_window(self):

        student = self.get_selected_student()

        if student is None:

            messagebox.showwarning(
                "No Student",
                "Please select a student first."
            )

            return

        exam_id = self.get_selected_exam_id()

        if exam_id is None:
            return

        exam = get_exam(
            exam_id
        )

        if exam is None:
            return

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Update Exam"
        )

        window.geometry(
            "450x500"
        )

        ttk.Label(
            window,
            text="Update Exam",
            font=("Arial", 14, "bold")
        ).pack(
            pady=15
        )

        frame = ttk.Frame(
            window,
            padding=15
        )

        frame.pack()

        fields = [
            ("Exam Name", exam[2]),
            ("Physics Maximum", exam[3]),
            ("Chemistry Maximum", exam[4]),
            ("Biology Maximum", exam[5]),
            ("Physics Marks", exam[6]),
            ("Chemistry Marks", exam[7]),
            ("Biology Marks", exam[8])
        ]

        entries = {}

        for index, (name, value) in enumerate(fields):

            ttk.Label(
                frame,
                text=name
            ).grid(
                row=index,
                column=0,
                sticky="w",
                pady=7
            )

            entry = ttk.Entry(
                frame,
                width=25
            )

            entry.insert(
                0,
                str(value)
            )

            entry.grid(
                row=index,
                column=1,
                padx=10,
                pady=7
            )

            entries[name] = entry

        def save():

            try:

                exam_name = (
                    entries["Exam Name"]
                    .get()
                    .strip()
                )

                physics_max = float(
                    entries["Physics Maximum"].get()
                )

                chemistry_max = float(
                    entries["Chemistry Maximum"].get()
                )

                biology_max = float(
                    entries["Biology Maximum"].get()
                )

                physics = float(
                    entries["Physics Marks"].get()
                )

                chemistry = float(
                    entries["Chemistry Marks"].get()
                )

                biology = float(
                    entries["Biology Marks"].get()
                )

                maximums = [
                    physics_max,
                    chemistry_max,
                    biology_max
                ]

                marks = [
                    physics,
                    chemistry,
                    biology
                ]

                if not exam_name:
                    raise ValueError(
                        "Exam name cannot be empty."
                    )

                if any(
                    maximum <= 0
                    for maximum in maximums
                ):
                    raise ValueError(
                        "Maximum marks must be greater than 0."
                    )

                for mark, maximum in zip(
                    marks,
                    maximums
                ):

                    if mark < 0 or mark > maximum:

                        raise ValueError(
                            "Marks must be between "
                            "0 and the maximum marks."
                        )

                update_exam(
                    exam_id,
                    exam_name,
                    physics_max,
                    chemistry_max,
                    biology_max,
                    physics,
                    chemistry,
                    biology
                )

                messagebox.showinfo(
                    "Success",
                    "Exam updated successfully."
                )

                window.destroy()

                self.load_student_data(
                    student
                )

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Input",
                    str(error)
                )

        ttk.Button(
            window,
            text="Update Exam",
            command=save
        ).pack(
            pady=15
        )

    # ========================================================
    # DELETE EXAM
    # ========================================================

    def delete_selected_exam(self):

        student = self.get_selected_student()

        if student is None:
            return

        exam_id = self.get_selected_exam_id()

        if exam_id is None:
            return

        exam = get_exam(
            exam_id
        )

        if exam is None:
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete exam '{exam[2]}'?"
        )

        if not confirm:
            return

        delete_exam(
            exam_id
        )

        messagebox.showinfo(
            "Deleted",
            "Exam deleted successfully."
        )

        self.load_student_data(
            student
        )

    # ========================================================
    # DELETE STUDENT
    # ========================================================

    def delete_selected_student(self):

        student = self.get_selected_student()

        if student is None:

            messagebox.showwarning(
                "No Student",
                "Please select a student first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete {student[1]} and all "
            "their exams?"
        )

        if not confirm:
            return

        delete_student(
            student[0]
        )

        messagebox.showinfo(
            "Deleted",
            "Student and all exams deleted."
        )

        self.student_title.config(
            text="Select a student"
        )

        self.refresh_students()

        self.set_text(
            self.dashboard_text,
            "Select a student."
        )

        self.set_text(
            self.analysis_text,
            "Select a student."
        )

        for item in self.exam_tree.get_children():
            self.exam_tree.delete(item)

    # ========================================================
    # COMPARE EXAMS
    # ========================================================

    def compare_selected_exams(self):

        student = self.get_selected_student()

        if student is None:
            return

        exams = get_student_exams(
            student[0]
        )

        if len(exams) < 2:

            messagebox.showwarning(
                "Not Enough Exams",
                "At least two exams are required."
            )

            return

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Compare Exams"
        )

        window.geometry(
            "400x300"
        )

        ttk.Label(
            window,
            text="Select two exams",
            font=("Arial", 13, "bold")
        ).pack(
            pady=15
        )

        ttk.Label(
            window,
            text="First Exam"
        ).pack()

        first = ttk.Combobox(
            window,
            state="readonly",
            width=35
        )

        first["values"] = [
            f"{exam[0]} | {exam[2]}"
            for exam in exams
        ]

        first.pack(
            pady=5
        )

        ttk.Label(
            window,
            text="Second Exam"
        ).pack()

        second = ttk.Combobox(
            window,
            state="readonly",
            width=35
        )

        second["values"] = first["values"]

        second.pack(
            pady=5
        )

        def compare():

            if not first.get() or not second.get():

                messagebox.showerror(
                    "Error",
                    "Please select both exams."
                )

                return

            first_id = int(
                first.get().split("|")[0].strip()
            )

            second_id = int(
                second.get().split("|")[0].strip()
            )

            if first_id == second_id:

                messagebox.showerror(
                    "Error",
                    "Please select two different exams."
                )

                return

            first_exam = get_exam(
                first_id
            )

            second_exam = get_exam(
                second_id
            )

            first_percentage, second_percentage, difference = (
                compare_exams(
                    first_exam,
                    second_exam
                )
            )

            if difference > 0:
                result = (
                    f"Improvement: "
                    f"+{difference:.2f} percentage points"
                )

            elif difference < 0:
                result = (
                    f"Decline: "
                    f"{difference:.2f} percentage points"
                )

            else:
                result = "No change."

            messagebox.showinfo(
                "Comparison",
                f"{first_exam[2]}: "
                f"{first_percentage:.2f}%\n\n"
                f"{second_exam[2]}: "
                f"{second_percentage:.2f}%\n\n"
                f"{result}"
            )

        ttk.Button(
            window,
            text="Compare",
            command=compare
        ).pack(
            pady=20
        )

    # ========================================================
    # EXPORT REPORT
    # ========================================================

    def export_report(self):

        student = self.get_selected_student()

        if student is None:
            return

        exams = get_student_exams(
            student[0]
        )

        if not exams:

            messagebox.showwarning(
                "No Data",
                "This student has no exam data."
            )

            return

        filename = filedialog.asksaveasfilename(
            title="Save Student Report",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if not filename:
            return

        success = export_student_report(
            student,
            exams,
            filename
        )

        if success:

            messagebox.showinfo(
                "Report Exported",
                f"Report saved successfully."
            )

    # ========================================================
    # GRAPHS
    # ========================================================

    def performance_graph(self):

        student = self.get_selected_student()

        if student is None:
            return

        exams = get_student_exams(
            student[0]
        )

        if not exams:

            messagebox.showwarning(
                "No Data",
                "This student has no exams."
            )

            return

        show_student_performance_graph(
            student[1],
            exams
        )

    def subject_graph(self):

        student = self.get_selected_student()

        if student is None:
            return

        exams = get_student_exams(
            student[0]
        )

        if not exams:
            return

        show_subject_comparison(
            student[1],
            exams
        )

    def trend_graph(self):

        student = self.get_selected_student()

        if student is None:
            return

        exams = get_student_exams(
            student[0]
        )

        if len(exams) < 2:

            messagebox.showwarning(
                "Not Enough Data",
                "At least two exams are required."
            )

            return

        show_subject_trends(
            student[1],
            exams
        )

    # ========================================================
    # RANKINGS
    # ========================================================

    def get_rankings(self):

        students = get_all_students()

        students_with_exams = []

        for student in students:

            exams = get_student_exams(
                student[0]
            )

            students_with_exams.append(
                (student, exams)
            )

        return calculate_student_rankings(
            students_with_exams
        )

    def show_rankings(self):

        rankings = self.get_rankings()

        if not rankings:

            messagebox.showinfo(
                "Rankings",
                "No student has exam data."
            )

            return

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Class Rankings"
        )

        window.geometry(
            "700x500"
        )

        columns = (
            "rank",
            "name",
            "average",
            "classification"
        )

        tree = ttk.Treeview(
            window,
            columns=columns,
            show="headings"
        )

        headings = {
            "rank": "Rank",
            "name": "Student",
            "average": "Average",
            "classification": "Performance"
        }

        for column in columns:

            tree.heading(
                column,
                text=headings[column]
            )

            tree.column(
                column,
                width=150
            )

        tree.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        for student in rankings:

            tree.insert(
                "",
                tk.END,
                values=(
                    student["rank"],
                    student["name"],
                    f"{student['average']:.2f}%",
                    student["classification"]
                )
            )

        statistics = calculate_class_statistics(
            rankings
        )

        ttk.Label(
            window,
            text=(
                f"Class Average: "
                f"{statistics['class_average']:.2f}%    "
                f"Median: "
                f"{statistics['median']:.2f}%    "
                f"Highest: "
                f"{statistics['highest']:.2f}%"
            ),
            font=("Arial", 10, "bold")
        ).pack(
            pady=10
        )

    def ranking_graph(self):

        rankings = self.get_rankings()

        if not rankings:

            messagebox.showwarning(
                "No Data",
                "No ranking data available."
            )

            return

        show_ranking_graph(
            rankings
        )


# ============================================================
# START GUI
# ============================================================

def start_gui():

    root = tk.Tk()

    app = MarksAnalyserGUI(
        root
    )

    root.mainloop()