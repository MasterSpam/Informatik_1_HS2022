import os
# see access for file
def get_average_grade(path):
    grades = []
    if not os.path.exists(path):
        return None

    with open(path) as my_grades:

        for line in my_grades.readlines():
            line = line.replace('\t', '')
            line = line.replace('\n', '')

            if len(line) == 0: continue
            if ''.join(line.split())[0] == '#': continue
            if line.find(':') == -1: continue

            grade = line.split(':')[1]
            grade = grade.strip()
            grades.append(float(grade))

    if len(grades) == 0: return 0.0
    return sum(grades) / len(grades)

    return -1

print(get_average_grade("public/my_grades.txt"))