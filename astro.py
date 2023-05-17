first_timestamp = input().split(":")
first_HH = int(first_timestamp[0])
first_MM = int(first_timestamp[1])
s_first_mm = first_timestamp[1]
second_timestamp = input().split(":")
second_HH = int(second_timestamp[0])
second_MM = int(second_timestamp[1])
s_second_mm = second_timestamp[1]
first_interval = input().split(":")
first_interval_HH = int(first_interval[0])
first_interval_MM = int(first_interval[1])
second_interval = input().split(":")
second_interval_HH = int(second_interval[0])
second_interval_MM = int(second_interval[1])

first_current_day = "Saturday"
second_current_day = "Saturday"

day_map = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
first_day_index = 0
second_day_index = 0

while True:
    if s_first_mm[1] != s_second_mm[1]:
        print("Never")
        break
    if (first_day_index + 1) * 200 + first_HH * 2 + first_MM * 0.2 < (
            second_day_index + 1) * 200 + second_HH * 2 + second_MM * 0.2:
        first_MM += first_interval_MM
        addH = int(first_MM / 60)
        first_MM = (first_MM % 60)
        first_HH += (addH + first_interval_HH)
        addD = int(first_HH / 24)
        first_HH = (first_HH % 24)
        first_day_index += addD
        first_day_index = first_day_index % 7

    elif (first_day_index + 1) * 200 + first_HH * 2 + first_MM * 0.2 > (
            second_day_index + 1) * 200 + second_HH * 2 + second_MM * 0.2:
        second_MM += second_interval_MM
        addH = int(second_MM / 60)
        second_MM = (second_MM % 60)
        second_HH += (addH + second_interval_HH)
        addD = int(second_HH / 24)
        second_HH = (second_HH % 24)
        second_day_index += addD
        second_day_index = second_day_index % 7

    elif (first_day_index + 1) * 200 + first_HH * 2 + first_MM * 0.2 == (
            second_day_index + 1) * 200 + second_HH * 2 + second_MM * 0.2:
        print(day_map[first_day_index])
        if len(str(first_MM)) == 1:
            first_MM = "0" + str(first_MM)
        if len(str(first_HH)) == 1:
            first_HH = "0" + str(first_HH)
        print(str(first_HH) + ":" + str(first_MM))
        break
