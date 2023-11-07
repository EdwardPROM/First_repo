def get_grade(ects_grade):
    grade_mapping = {
        "F": 1,
        "FX": 2,
        "E": 3,
        "D": 3,
        "C": 4,
        "B": 5,
        "A": 5
    }
    
    return grade_mapping.get(ects_grade)

def get_description(ects_grade):
    description_mapping = {
        "F": "Unsatisfactorily",
        "FX": "Unsatisfactorily",
        "E": "Enough",
        "D": "Satisfactorily",
        "C": "Good",
        "B": "Very good",
        "A": "Perfectly"
    }
    
    return description_mapping.get(ects_grade)

# Приклад використання:
ects_grade = "E"
grade = get_grade(ects_grade)
description = get_description(ects_grade)

if grade is not None:
    print(f"П'ятибальна оцінка: {grade}")
    print(f"Пояснення: {description}")
else:
    print("Невідома оцінка ECTS")