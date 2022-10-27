import os


def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False

    file_read = open(path_reading, "r")
    file_write = open(path_writing, "w")
    all_lines = file_read.readlines()

    for i in range(len(all_lines)):
        print(all_lines[i])
        if i == 0:
            file_write.write("Firstname,Lastname" + ('\n' if len(all_lines) > 1 else ''))

        elif all_lines[i] == "\n":
            file_write.write(",\n")

        elif ";" in all_lines[i]:
            if i < len(all_lines) - 1:
                file_write.write(all_lines[i][all_lines[i].find(";") + 2:-1] + "," + all_lines[i][:all_lines[i].find(";")] + "\n")
            else:
                file_write.write(all_lines[i][all_lines[i].find(";") + 2:] + "," + all_lines[i][:all_lines[i].find(";")])
        else:
            file_write.write(all_lines[i][:all_lines[i].find(" ")] + "," + all_lines[i][all_lines[i].find(" ") + 1:])

    file_write.close()
    file_read.close()


INPUT_PATH = "my_data.txt"
OUTPUT_PATH = "my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
