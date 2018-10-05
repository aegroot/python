studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    per_student1 = (sum((sum(studentencijfers[0])) / 3))
    per_student2 = (sum((sum(studentencijfers[1])) / 3))
    per_student3 = (sum((sum(studentencijfers[2])) / 3))
    gemps = per_student1 + per_student2 + per_student3


def gemiddelde_van_alle_studenten(studentencijfers):
    all_stud = sum(studentencijfers[0]) + sum(studentencijfers[1]) + sum(studentencijfers[2])
    return all_stud


print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
