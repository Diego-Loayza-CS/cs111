### Implement your code in this file.


def append(split_data, section, i):
    section.append(int(split_data[i][1]))


def extract_grades(split_data, section):
    i = 0
    while split_data[i] != ["\n"]:
        if len(split_data[i]) == 2:
            append(split_data, section, i)
        i += 1


def update_list(split_data):
    i = 0
    while split_data[i] != ["\n"]:
        split_data.pop(i)
    while split_data[i] == ["\n"]:
        split_data.pop(i)


def drop_lowest(section, i):
    n = 0
    section.sort()
    while n != i:
        section.pop(0)
        n += 1


def decide_grade(student_percentage):
    if student_percentage < 60:
        return "E"
    elif student_percentage < 63:
        return "D-"
    elif student_percentage < 67:
        return "D"
    elif student_percentage < 70:
        return "D+"
    elif student_percentage < 73:
        return "C-"
    elif student_percentage < 77:
        return "C"
    elif student_percentage < 80:
        return "C+"
    elif student_percentage < 83:
        return "B-"
    elif student_percentage < 87:
        return "B"
    elif student_percentage < 90:
        return "B+"
    elif student_percentage < 93:
        return "A-"
    else:
        return "A"


def main():
    # ABRIR ARCHIVO
    filename = input("Please enter the grade data filename: ")
    with open(filename, "r") as grades_file:

        # SEPARAR DATOS
        all_data = grades_file.readlines()
        split_data = []
        i = 0
        while i < len(all_data):
            split_data.append(all_data[i].split(","))
            i += 1

        # ORGANIZAR DATOS
        labs = []
        homework = []
        projects = []
        midterm1 = []
        midterm2 = []
        final = []

    if split_data[0] == ['# Labs\n']:
        extract_grades(split_data, labs)
        update_list(split_data)

    if split_data[0] == ['# Homework\n']:
        extract_grades(split_data, homework)
        update_list(split_data)

    if split_data[0] == ['# Projects\n']:
        extract_grades(split_data, projects)
        update_list(split_data)

    if split_data[0] == ['# Exams\n']:
        i = 0
        while split_data[i] != ["\n"]:
            if len(split_data[i]) == 2:

                if split_data[i][0] == "Midterm1":
                    append(split_data, midterm1, i)

                elif split_data[i][0] == "Midterm2":
                    append(split_data, midterm2, i)

                elif split_data[i][0] == "Final":
                    append(split_data, final, i)
            i += 1

    # REPORTE DE NOTAS
    print(f"""Here are the student's grades:
Category     Points     Percentage""")


    all_weights = []
    accumulated_weights = []

    if len(labs) >= 1:
        drop_lowest(labs, 2)
        labs_score = sum(labs)
        labs_total = len(labs) * 20
        labs_percent = round((labs_score / labs_total) * 100, 1)
        labs_weight = labs_percent * 0.10
        all_weights.append(labs_weight)
        print(f"Labs:        {labs_score}/{labs_total}    {labs_percent:.1f}%")
        accumulated_weights.append(0.10)

    if len(homework) >= 1:
        drop_lowest(homework, 1)
        hw_score = sum(homework)
        hw_total = len(homework) * 50
        hw_percent = round((hw_score / hw_total) * 100, 1)
        hw_weight = hw_percent * 0.15
        all_weights.append(hw_weight)
        print(f"Homework:    {hw_score}/{hw_total}    {hw_percent:.1f}%")
        accumulated_weights.append(0.15)

    if len(projects) >= 1:
        proj_score = sum(projects)
        proj_total = len(projects) * 100
        proj_percent = round((proj_score / proj_total) * 100, 1)
        proj_weight = proj_percent * 0.25
        all_weights.append(proj_weight)
        print(f"Projects:    {proj_score}/{proj_total}    {proj_percent:.1f}%")
        accumulated_weights.append(0.25)

    if len(midterm1) == 1:
        midterm1 = midterm1[0]
        midterm1_percent = round(midterm1 * 2.5, 1)
        midterm1_weight = midterm1_percent * 0.15
        all_weights.append(midterm1_weight)
        print(f"Midterm 1:     {midterm1}/40    {midterm1_percent:.1f}%")
        accumulated_weights.append(0.15)

    if len(midterm2) == 1:
        midterm2 = midterm2[0]
        midterm2_percent = round(midterm2 * 2.5, 1)
        midterm2_weight = midterm2_percent * 0.15
        all_weights.append(midterm2_weight)
        print(f"Midterm 2:     {midterm2}/40    {midterm2_percent:.1f}%")
        accumulated_weights.append(0.15)

    if len(final) == 1:
        final = final[0]
        final_percent = round(final * (10 / 7), 1)
        final_weight = final_percent * 0.20
        all_weights.append(final_weight)
        print(f"Final:         {final}/70    {final_percent:.1f}%")
        accumulated_weights.append(0.20)

    # NOTA FINAL
    student_percentage = round(sum(all_weights) / sum(accumulated_weights), 2)
    overall_grade = decide_grade(student_percentage)
    print(f"""
The overall grade in the class is: {overall_grade} ({student_percentage:.2f}%)""")


if __name__ == '__main__':
    main()
