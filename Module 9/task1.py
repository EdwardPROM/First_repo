def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)

def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)

def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description
    else:
        return None

# Приклад використання:
student_grade_function = get_student_grade("grade")
grade_result = student_grade_function("A")
print("Grade result:", grade_result)

student_description_function = get_student_grade("description")
description_result = student_description_function("A")
print("Description result:", description_result)

invalid_option_function = get_student_grade("invalid_option")
print("Invalid option result:", invalid_option_function)

