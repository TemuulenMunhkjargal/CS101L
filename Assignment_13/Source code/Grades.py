import math
import statistics

def total(values):
    sum = float()
    for num in values:
        sum += num
    return sum

def average(values):
    try:
        sum = float()
        for num in values:
            sum += num
        avg = sum / len(values)
        return avg
    except ZeroDivisionError:
        return math.nan


def median(values):
    if len(values):
        med = statistics.median(values)
        return med
    else:
        raise ValueError

        