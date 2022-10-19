
def hamming_dist(signal_1, signal_2):

    hamming_distances = []
    data_set1 = signal_1["data"]
    data_set2 = list(signal_2)

    if len(data_set1) != len(data_set2) or not data_set1 or not data_set2:
        return "Empty signal on at least one of the sensors"

    for data1, data2 in zip(data_set1, data_set2):
        difference = 0
        if len(data1) != len(data2):
            return "Sensor defect detected"

        for i in range(len(data1)):
            if data1[i] != data2[i]:
                difference += 1

        if difference > 0:
            hamming_distances.append((data1, data2, difference))

    return hamming_distances


signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")

print(hamming_dist(signal_sensor_1, signal_sensor_2))
