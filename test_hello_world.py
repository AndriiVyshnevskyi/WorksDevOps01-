# test_hello_world.py

import unittest
from io import StringIO
import sys

sys.path.append('/home/vishnia/git/WorksDevOps01-/')
from hello_world import words

class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        words()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, world!\n")

if __name__ == "__main__":
    unittest.main()

