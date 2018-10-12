import csv
import math
import pprint

from settings import (
    ACTIONS,
    ALLOWED_DAYS,
    INDEXED_DAYS
)

def get_line_index(items):
    line_index = {}
    for i, item in enumerate(items):
        item = item.strip()
        if '-' in item:
            ranged = get_day_range(item)
            for r in ranged:
                line_index[r] = i
        else:
            line_index[item] = i
    return line_index


def get_day_range(item):
    """
    Given a day range, return the constituent days
    """
    ranged = []
    values = item.split('-')
    start = values[0]
    end = values[1]
    range_values = INDEXED_DAYS

    for i in range (INDEXED_DAYS[start], INDEXED_DAYS[end] + 1):
        ranged.append(ALLOWED_DAYS[i])

    if ranged == []:
        raise ValueError('The ranged days value is incorrect: {}'.format(item))

    return ranged


def parse_csv(file_path):
    """
    Given the file path to a csv file of max 2 lines,
    return the processed contents
    """
    data = []
    with open(file_path, 'r') as f:
        week_list = []
        reader = csv.reader(f)
        indices = get_line_index(next(reader))

        for line in reader:
            for day in ALLOWED_DAYS:
                processed = {}
                day_value = int(line[indices[day]])
                day_desc = line[indices['description']]
                resolved_day_value = get_resolved_day_value(day, day_value)

                processed['day'] = day
                processed['description'] = str(day_desc) + " " + \
                    str(resolved_day_value)
                processed[ACTIONS[day]] = resolved_day_value
                processed['value'] = day_value
                week_list.append(processed)
    return week_list

def get_resolved_day_value(day, day_value):

    day_type = ACTIONS[day]
    day_value = float(day_value)

    if day_type == 'square':
        return int(math.pow(day_value, 2))

    if day_type == 'double':
        return int(day_value * 2)
