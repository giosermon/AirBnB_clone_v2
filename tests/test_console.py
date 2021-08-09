#!/usr/bin/python3
"""This module tests console.py file.
Usage:
    To be used with the unittest module:
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_console.py"
"""
import unittest
import os


class TestConsole(unittest.TestCase):
    ''' TestCase class for storing the unittests of the console. '''

    def test_create(self):
        ''' Tests for the create command. '''
        # Create console session.

    @classmethod
    def tearDown(self):
        ''' Removes the file.json on each test. '''
        try:
            os.remove("file.json")
        except:
            pass


if __name__ == "__main__":
    unittest.main()
