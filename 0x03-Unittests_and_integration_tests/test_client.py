#!/usr/bin/env python3
"""Unit testing for client module"""

import unittest
from typing import Dict
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import get_json, GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing org method"""

    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get: Mock):
        """Test org name"""
        payload: Dict[str, str] = {"org_name": org_name}

        mock_get.return_value = lambda: payload
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org(), payload)
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
