grades_by_course = {
    "Matematik": [70, 85, 90],
    "Türkçe": [80, 88, 92],
    "Fizik": [75, 82, 88],
}
averages = {}

for ders, notlar in grades_by_course.items():
    averages[ders] = sum(notlar) / len(notlar)


    for ders, ort in averages.items():
        print(f"{ders}: {ort:.2f}")