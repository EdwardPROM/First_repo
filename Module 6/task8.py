def save_applicant_data(source, output):
    with open(output, 'w') as output_file:
        for applicant in source:
            # Формуємо рядок для запису в файл
            data_line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
            # Записуємо рядок у файл
            output_file.write(data_line)

# Приклад виклику функції
applicants_data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

output_file_path = 'output.txt'
save_applicant_data(applicants_data, output_file_path)
