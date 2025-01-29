# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


# define your functions here
def convert_row_type(row):
    float_row = []
    for item in row:
        float_row.append(float(item))
    return float_row


def normalized_gpa(gpa):
    return gpa * 2


def normalized_sat(sat):
    return sat / 160


def calculate_score(list_scores):
    result = round(
        (normalized_sat(list_scores[0]) * 0.3) + (normalized_gpa(list_scores[1]) * 0.4) + (list_scores[2] * 0.1) + (
                list_scores[3] * 0.2),
        2)
    return result


def is_outlier(score):
    return score[2] == 0 or normalized_gpa(score[1]) - normalized_sat(score[0]) > 2


def calculate_score_improved(list_scores):
    student_score = calculate_score(list_scores)
    return is_outlier(list_scores) or student_score >= 6


def grade_outlier(grade_list):
    sorted_list = sorted(grade_list)
    return sorted_list[1] - sorted_list[0] > 20


def grade_improvement(grade_list):
    semester2 = grade_list[1] >= grade_list[0]
    semester3 = grade_list[2] >= grade_list[1] and grade_list[2] >= grade_list[0]
    semester4 = grade_list[3] >= grade_list[2] and grade_list[3] >= grade_list[1] and grade_list[3] >= grade_list[0]
    return semester2 and semester3 and semester4


def main():
    # ABRIR ARCHIVO
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")

    # LISTAS DE SETS SIN HEADER
    data = input_file.readlines()
    i = 1
    values = []
    while i < len(data):
        values.append(data[i].split(","))
        i += 1

    # GUARDAR NOMBRES Y BORRAR
    names = []
    for value in values:
        names.append(value[0])
        value.pop(0)

    # CONVERTIR A FLOATS
    float_lists = []
    for string in values:
        float_row = convert_row_type(string)
        float_lists.append(float_row)

    # VERIFICAR LISTAS
    for row in float_lists:
        check_row_types(row)

    # SEPARAR LISTAS
    raw_scores = []
    semester_grades = []
    for row in float_lists:
        raw_scores.append(row[0:4:])
        semester_grades.append(row[4::])

    # EXPORTAR (NOMBRE + SCORE)
    with open("student_scores.csv", "w") as exporting_file:
        count = 0
        final_scores = []
        for score in raw_scores:
            final_scores.append(calculate_score(score))
        while count < len(names):
            exporting_file.writelines(f"{names[count]},{final_scores[count]:.2f}\n")
            count += 1

    # EXPORTAR SELECCIONADOS
    with open("chosen_students.csv", "w") as chosens_file:
        index = 0
        while index < len(final_scores):
            if final_scores[index] >= 6:
                chosens_file.writelines(f"{names[index]}\n")
            index += 1

    # EXPORTAR OUTLIERS
    with open("outliers.csv", "w") as outliers_file:
        x = 0
        while x < len(raw_scores):
            if is_outlier(raw_scores[x]):
                outliers_file.writelines(f"{names[x]}\n")
            x += 1

    # EXPORTAR SELECCIONADOS + OUTLIERS con 5p+
    with open("chosen_improved.csv", "w") as chosen_improved_file:
        y = 0
        while y < len(names):
            if final_scores[y] >= 6 or (is_outlier(raw_scores[y]) and final_scores[y] >= 5):
                chosen_improved_file.writelines(f"{names[y]}\n")
            y += 1

    # EXPORTAR BETTER IMPROVED
    with open("better_improved.csv", "w") as better_improved_file:
        z = 0
        while z < len(names):
            if calculate_score_improved(raw_scores[z]):
                better_improved_file.writelines(
                    f"{names[z]},{raw_scores[z][0]},{raw_scores[z][1]},{raw_scores[z][2]},{raw_scores[z][3]}\n")
            z += 1

    # EXPORTAR TODAS LAS CONDICIONES
    with open("composite_chosen.csv", "w") as composite_chosen_file:
        a = 0
        while a < len(names):
            print(f"""
DEBUG:
TEST FOR {a}

{final_scores[a]} >= 6   or   {final_scores[a]}     with at least one of
{is_outlier(raw_scores[a])} (is outlier: {raw_scores[a]})    or    {grade_outlier(semester_grades[a])}  (grade outlier: {semester_grades[a]})  or    {grade_improvement(semester_grades[a])} (grade improvement)

which is
{final_scores[a] >= 6 or final_scores[a] >= 5 and is_outlier(raw_scores[a]) or grade_outlier(semester_grades[a]) or grade_improvement(semester_grades[a])}
        
        
            """)

            if final_scores[a] >= 6 or (final_scores[a] >= 5 and (is_outlier(raw_scores[a]) or grade_outlier(semester_grades[a]) or grade_improvement(semester_grades[a]))):
                composite_chosen_file.writelines(f"{names[a]}\n")
            a += 1


    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()

    # TODO: loop through the rest of the file
    # TODO: make sure to close all files you've opened!

    print("done!")


# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
