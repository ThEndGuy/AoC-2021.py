#!/usr/bin/env python

INPUT_FILE = "input.txt"

def normal_measurement_counter(_file):
    with open(_file , "r") as f:
        text = f.readlines()
        prev_number = None
        measures = 0
        for number in text:
            number = int(number.strip("\n"))
            if not prev_number:
                prev_number = number
                continue
            if prev_number < number:
                measures += 1
            prev_number = number
    return measures

print(normal_measurement_counter(INPUT_FILE))


def triplet_measurement_counter(_file):
    with open(_file , "r") as f:
        text = f.readlines()
        prev_sum = None
        measures = 0
        text = [int(num.strip("\n")) for num in text]
        for i, number in enumerate(text):
            if i == len(text) - 2:
                break
            summ = number + text[i + 1] + text[i + 2]
            print(summ)
            if not prev_sum:
                prev_sum = summ
                continue
            if prev_sum < summ:
                measures += 1
            prev_sum = summ
    return measures

print(triplet_measurement_counter(INPUT_FILE))
