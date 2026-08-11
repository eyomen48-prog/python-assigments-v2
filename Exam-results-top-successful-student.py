students = [
    {"name": "Ali", "score": 85},
    {"name": "Ayşe", "score": 92},
    {"name": "Mehmet", "score": 88}
]
sirali = sorted(students, key=lambda x: x["score"], reverse =True)
print(sirali[0]["name"])