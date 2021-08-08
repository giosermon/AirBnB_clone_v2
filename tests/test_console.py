#!/usr/bin/python3
"""This module tests console.py file.
Usage:
    To be used with the unittest module:
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_console.py"
"""
# from models.engine.file_storage import FileStorage as Storage
from models.__init__ import storage
from unittest.mock import create_autospec, patch
from console import HBNBCommand
from io import StringIO
import unittest
import pep8
import sys
import os


classes = ["User", "State", "City", "Amenity", "Place", "Review"]
# Storage = Storage()


class TestConsole(unittest.TestCase):
    ''' TestCase class for storing the unittests of the console. '''

    def test_create_00(self):
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
