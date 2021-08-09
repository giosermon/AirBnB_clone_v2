#!/usr/bin/python3
"""
Console testing Suite
"""

from console import HBNBCommand
import unittest
from unittest.mock import create_autospec, patch
import sys
from io import StringIO
import os


MSG_MISSING = '** class name missing **'


class TestConsole(unittest.TestCase):

    def teardown(cls):
        ''' Delete File'''
        try:
            os.remove("file.json")
        except:
            pass

    def setUp(self):
        ''' Sets up the mock stdin and stderr. '''
        self.mock_stdout = create_autospec(sys.stdout)

    def get_cli(self):
        '''create console instance with mock in and out'''
        stdin = create_autospec(sys.stdin)
        stdout = create_autospec(sys.stdin)
        return HBNBCommand(stdin=stdin, stdout=stdout)

    def test_create(self):
        ''' Tests for the create command. '''
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            output = Output.getvalue().strip()
            self.assertFalse(cli.onecmd('create'))

        self.assertEqual(MSG_MISSING, output)
