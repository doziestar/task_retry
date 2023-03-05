#!/usr/bin/env python

"""Tests for `task_retry` package."""

import pytest

from click.testing import CliRunner

from task_retry import task_retry
from task_retry import cli
import unittest
from unittest.mock import Mock
from task_retry import RetryOptions


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'task_retry.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


class RetryOptionsTests(unittest.TestCase):
    def test_delay(self):
        retry_options = RetryOptions()
        self.assertEqual(retry_options.delay(1), retry_options.delay_factor)
        self.assertEqual(retry_options.delay(2), retry_options.delay_factor * 2.0)
        self.assertLessEqual(retry_options.delay(8), retry_options.max_delay)

    def test_retry(self):
        retry_options = RetryOptions(max_attempts=3)
        fn = Mock()
        fn.side_effect = [Exception(), Exception(), 'success']
        result = retry_options.retry(fn)
        self.assertEqual(result, 'success')
        self.assertEqual(fn.call_count, 3)

    def test_retry_if(self):
        retry_options = RetryOptions()
        fn = Mock()
        fn.side_effect = [ValueError(), Exception()]
        retry_if = lambda e: isinstance(e, ValueError)
        result = retry_options.retry(fn, retry_if=retry_if)
        self.assertIsNone(result)
        self.assertEqual(fn.call_count, 1)

    def test_on_retry(self):
        retry_options = RetryOptions()
        fn = Mock()
        fn.side_effect = [Exception(), 'success']
        on_retry = Mock()
        result = retry_options.retry(fn, on_retry=on_retry)
        self.assertEqual(result, 'success')
        self.assertEqual(on_retry.call_count, 1)

    def test_max_attempts(self):
        retry_options = RetryOptions(max_attempts=2)
        fn = Mock()
        fn.side_effect = Exception()
        with self.assertRaises(Exception):
            retry_options.retry(fn)
        self.assertEqual(fn.call_count, 2)
        

class TestRetryOptionsDecorator(unittest.TestCase):
    def test_retry_decorator(self):
        class MockClass:
            def __init__(self):
                self.num_attempts = 0

            @task_retry.RetryOptionsDecorator()
            def mock_method(self):
                self.num_attempts += 1
                if self.num_attempts < 5:
                    raise ValueError("Failed attempt")
                return "Success"

        obj = MockClass()
        result = obj.mock_method()

        self.assertEqual(result, "Success")
        self.assertEqual(obj.num_attempts, 5)


if __name__ == '__main__':
    unittest.main()
