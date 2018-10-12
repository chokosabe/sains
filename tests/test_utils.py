import ast
import os
import csv
from unittest import (
    TestCase
)

from settings import (
    ALLOWED_DAYS,
    MAX_LINES
)
from utils.dow import (
    get_day_range,
    get_line_index,
    get_resolved_day_value,
    parse_csv
)


class TestUtils(TestCase):


    def setUp(self):
        self.csv1 = '/tests/data/1.csv'
        self.csv2 = '/tests/data/2.csv'
        self.csv3 = '/tests/data/3.csv'

        self.expected1 = 'tests/data/expected1.txt'
        self.expected2 = 'tests/data/expected2.txt'
        self.expected3 = 'tests/data/expected3.txt'

        self.lines_types_file = '/tests/data/line_types.csv'

    def test_test_pickup(self):
        print('Picked up test')

    def test_get_day_range_correct(self):
        """
        """
        days = "mon-fri"
        result = get_day_range(days)
        self.assertEqual(result, ALLOWED_DAYS)

        days2 = "mon-wed"
        res = get_day_range(days2)
        self.assertEqual(res, ALLOWED_DAYS[:3])

    def test_get_day_range_incorrect_range(self):
        """
        """
        days3 = "wed-mon"
        with self.assertRaises(ValueError):
            res = get_day_range(days3)

    def test_get_line_index(self):
        """
        """
        line_data_file = os.getcwd() + self.lines_types_file
        with open(line_data_file, 'r') as f:
            for line in f:
                line_data = line.split('|')
                res = get_line_index(line_data[0].strip().split(','))
                expected = line_data[1].strip().split(',')
                expected = [int(x) for x in expected]
                self.assertEqual(list(res.values()), expected)

    def test_get_resolved_day_value_square(self):
        """
        """
        day = 'mon'
        day_value = 3
        res = get_resolved_day_value(day, day_value)
        self.assertEqual(res, 9)

    def test_get_resolved_day_value_double(self):
        """
        """
        day = 'fri'
        day_value = 4
        res = get_resolved_day_value(day, day_value)
        self.assertEqual(res, 8)


    def test_parse_csv1(self):
        """
        """
        file_path = os.getcwd() + self.csv1
        res = parse_csv(file_path)
        with open(self.expected1, 'r') as expected1:
            expected = ast.literal_eval(expected1.read())
            self.assertEqual(res, expected)

    def test_parse_csv2(self):
        """
        """
        file_path = os.getcwd() + self.csv2
        res = parse_csv(file_path)
        with open(self.expected2, 'r') as expected2:
            expected = ast.literal_eval(expected2.read())
            self.assertEqual(res, expected)

    def test_parse_csv3(self):
        """
        """
        file_path = os.getcwd() + self.csv3
        res = parse_csv(file_path)
        with open(self.expected3, 'r') as expected3:
            expected = ast.literal_eval(expected3.read())
            self.assertEqual(res, expected)
