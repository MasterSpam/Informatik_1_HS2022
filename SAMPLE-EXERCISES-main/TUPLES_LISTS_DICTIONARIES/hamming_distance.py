# ACCESS SOLUTION

def hamming_dist(signal_1, signal_2):
    if not (0 < len(signal_1["data"]) == len(signal_2) > 0):
        print("Empty sensor signal") # the print statements are optional
        return "Empty signal on at least one of the sensors"
    output = []
    for code_1, code_2 in zip(signal_1["data"], signal_2):
        if len(code_1) != len(code_2):
            print("Sensors send signals of different lengths") # the print statements are optional
            return "Sensor defect detected"
        distance = 0
        for index in range(len(code_1)):
            if code_1[index] != code_2[index]: distance += 1
        if distance > 0:
            output.append((code_1, code_2, distance))
    return output


signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))

