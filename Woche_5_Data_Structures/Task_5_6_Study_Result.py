
import os


def get_average_grade(path):

    all_marks = []

    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        for line in f.readlines():
            line = line[:-1]                    # remove \n
            if "#" not in line and len(line):
                if line.split(":")[1]:
                    all_marks.append(float(line.split(":")[1]))

    my_sum = sum(all_marks)
    if len(all_marks):
        return my_sum / len(all_marks)
    else:
        return 0.0


print(get_average_grade("my_grades.txt"))
# print(get_average_grade("public/my_grades.txt"))

