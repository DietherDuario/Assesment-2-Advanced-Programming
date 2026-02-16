import tkinter as tk
from tkinter import ttk, messagebox

def load_data(filename):
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        total = int(lines[0])
        for line in lines[1:]:
            parts = [p.strip() for p in line.split(",")]
            code = int(parts[0])
            name = parts[1]
            c1, c2, c3, exam = map(int, parts[2:])
            course_total = c1 + c2 + c3
            overall = course_total + exam
            percent = (overall / 160) * 100
            grade = get_grade(percent)
            students.append({
                "code": code,
                "name": name,
                "course": course_total,
                "exam": exam,
                "percent": percent,
                "grade": grade
            })
    return students, total

def get_grade(p):
    if p >= 70: return "A"
    elif p >= 60: return "B"
    elif p >= 50: return "C"
    elif p >= 40: return "D"
    else: return "F"

def show_student_info(s):
    text = (
        f"Name: {s['name']}\n"
        f"Student Number: {s['code']}\n"
        f"Coursework Total: {s['course']}/60\n"
        f"Exam Mark: {s['exam']}/100\n"
        f"Overall %: {s['percent']:.2f}%\n"
        f"Grade: {s['grade']}\n"
        "-----------------------------------"
    )
    return text

def show_all_students():
    output_box.delete("1.0", tk.END)
    total_pct = 0
    for s in students:
        output_box.insert(tk.END, show_student_info(s) + "\n")
        total_pct += s["percent"]
    avg = total_pct / total_students
    output_box.insert(tk.END, f"\nTotal Students: {total_students}\n")
    output_box.insert(tk.END, f"Average Percentage: {avg:.2f}%\n")

def show_individual():
    name = student_var.get()
    output_box.delete("1.0", tk.END)
    if not name:
        messagebox.showinfo("Info", "Please select a student.")
        return
    for s in students:
        if s["name"] == name:
            output_box.insert(tk.END, show_student_info(s))
            return
    messagebox.showerror("Error", "Student not found.")

def show_highest():
    output_box.delete("1.0", tk.END)
    top = max(students, key=lambda s: s["percent"])
    output_box.insert(tk.END, "Student with Highest Total Score:\n\n")
    output_box.insert(tk.END, show_student_info(top))

def show_lowest():
    output_box.delete("1.0", tk.END)
    low = min(students, key=lambda s: s["percent"])
    output_box.insert(tk.END, "Student with Lowest Total Score:\n\n")
    output_box.insert(tk.END, show_student_info(low))

def quit_program():
    root.destroy()

root = tk.Tk()
root.title("Student Manager")
root.geometry("600x500")
root.config(bg="#e6f0ff")

students, total_students = load_data("marks.txt")

frame_top = tk.Frame(root, bg="#e6f0ff")
frame_top.pack(pady=10)

tk.Label(frame_top, text="Select Student:", bg="#e6f0ff").pack(side=tk.LEFT, padx=5)
student_var = tk.StringVar()
names = [s["name"] for s in students]
student_menu = ttk.Combobox(frame_top, textvariable=student_var, values=names, width=30)
student_menu.pack(side=tk.LEFT)


frame_buttons = tk.Frame(root, bg="#e6f0ff")
frame_buttons.pack(pady=10)

btn_all = tk.Button(frame_buttons, text="View All", width=20, command=show_all_students)
btn_all.grid(row=0, column=0, padx=5, pady=5)

btn_individual = tk.Button(frame_buttons, text="View Individual", width=20, command=show_individual)
btn_individual.grid(row=0, column=1, padx=5, pady=5)

btn_highest = tk.Button(frame_buttons, text="Highest Score", width=20, command=show_highest)
btn_highest.grid(row=1, column=0, padx=5, pady=5)

btn_lowest = tk.Button(frame_buttons, text="Lowest Score", width=20, command=show_lowest)
btn_lowest.grid(row=1, column=1, padx=5, pady=5)

btn_quit = tk.Button(root, text="Quit", bg="lightcoral", command=quit_program)
btn_quit.pack(pady=5)

output_box = tk.Text(root, height=15, width=70, wrap="word", bg="white")
output_box.pack(pady=10)

root.mainloop()
