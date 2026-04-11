import matplotlib.pyplot as plt

students_names = ["sanjay", "rahul", "karan", "wasim", "ramish", "ajay", "sartaj", "priya"]
students_marks = [35, 50, 20, 45, 25, 40, 25, 40]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def marks_line_chart():
    plt.plot(students_names, students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

marks_line_chart()

def percentage_bar_chart():
    plt.bar(students_names, students_marks)
    plt.title("Students' Percentage Graph")
    plt.xlabel("Studnts Names")
    plt.ylabel("Students Percentage")
    plt.show()

percentage_bar_chart()


def percentage_line_chart():
    plt.line(students_names, students_marks)
    plt.label("students' percentage Graph")
    plt.xlabel