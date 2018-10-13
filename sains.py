"""
Run the Sains program
python3 -m sains
"""


import cmd
import os
import sys

import pprint
import pytest

from utils.dow import (
    parse_csv
)

bar = '==' * 32
data_dir = os.getcwd() + '/tests/data/'

def run_tests():
    sys.call()


def process_csv(name):
    """
    Process the named CSV
    """
    file_path = data_dir + name
    res = parse_csv(file_path)
    pprint.pprint(bar)
    pprint.pprint(res)
    pprint.pprint(bar)

class SainsInterface(cmd.Cmd):
    """
    Simple interface for this script
    """

    prompt = """
                0. Run all the tests
                1. Process and Print CSV1
                2. Process and Print CSV2
                3. Process and Print CSV3
                3. Quit
             """

    def do_0(self, args):
        pytest.main(['--verbose'])
        sys.exit(0)

    def do_1(self, args):
        process_csv('1.csv')
        sys.exit(0)

    def do_2(self, args):
        process_csv('2.csv')
        sys.exit(0)

    def do_3(self, args):
        process_csv('3.csv')
        sys.exit(0)


interface = SainsInterface()
interface.cmdloop(intro=None)
