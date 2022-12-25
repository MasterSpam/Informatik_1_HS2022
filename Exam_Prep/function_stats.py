
def stats(data):

    avg_students = {}
    avg_subjects = {}

    for mat_num in data:
        all_grades = []
        for subject in data[mat_num]:
            all_grades.append(subject[1])
            if subject[0] in avg_subjects:
                avg_subjects[subject[0]].append(subject[1])
            else:
                avg_subjects[subject[0]] = [subject[1]]

        avg_students[mat_num] = round(sum(all_grades) / len(all_grades), 2)

    for subject in avg_subjects:
        avg_subjects[subject] = round(sum(avg_subjects[subject]) / len(avg_subjects[subject]), 2)

    return avg_students, avg_subjects


# DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
raw = {"12-345-678": [("Math", 5.5), ("Biology", 5.75), ("Latin", 4.25)],
       "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
       "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
       }
students, subjects = stats(raw)
assert (len(students) == 3)
assert (len(subjects) == 4)
assert (students["12-345-678"] == 5.17)
assert (subjects["Latin"] == 4.08)
