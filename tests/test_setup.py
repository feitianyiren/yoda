# coding=utf-8
from unittest import TestCase
from click.testing import CliRunner

import yoda


class TestHealth(TestCase):
    """
        Test for the following commands:

        | Module: health
        | command: health
    """

    def __init__(self, methodName='runTest'):
        super(TestHealth, self).__init__()
        self.runner = CliRunner()

    def runTest(self):
        result = self.runner.invoke(yoda.cli, ['setup'])
        self.assertEqual(result.exit_code, 0)

        result = self.runner.invoke(yoda.cli, ['setup', 'check'])
        self.assertEqual(result.exit_code, 0)

        result = self.runner.invoke(yoda.cli, ['setup', 'new'], input="\n"
                                                                      "MP"
                                                                      "\n"
                                                                      "a"
                                                                      "\n"
                                                                      "\n"
                                                                      "mp"
                                                                      "\n"
                                                                      "\n"
                                                                      "mp"
                                                                      "\n"
                                                                      "~/.yoda/")
        self.assertEqual(result.exit_code, 0)

        result = self.runner.invoke(yoda.cli, ['setup', 'delete'])
        self.assertEqual(result.exit_code, 0)

        result = self.runner.invoke(yoda.cli, ['setup', 'check'])
        self.assertEqual(result.exit_code, 0)

        result = self.runner.invoke(yoda.cli, ['setup', 'invalid_argument'])
        self.assertEqual(result.exit_code, 0)
