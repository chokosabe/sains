"""
Run the Sains program
python3 -m sains
"""


import cmd
import sys

from utils.dow import (
    parse_csv
)

bar = '==' * 32

def run_tests():
    sys.call()


def process_csv(name):
    """
    Process the named CSV
    """
    pass


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
        run_tests()
        sys.exit(0)

    def do_1(self, args):
        process_csv('csv1')
        sys.exit(0)

    def do_2(self, args):
        process_csv('csv2')
        sys.exit(0)

    def do_3(self, args):
        process_csv('csv3')
        sys.exit(0)


interface = SainsInterface()
interface.cmdloop(intro=None)
