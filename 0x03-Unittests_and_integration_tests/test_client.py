#!/usr/bin/env python3

"""
Title: Unittests and integration tests of client script
Description: Testing Module designed to test the client module
Authors: @a_idk
"""

import json
import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing Github Org Client clas
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """
        Testing the GithubOrgClient.org method
        """

        class_tst = GithubOrgClient(input)
        class_tst.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """
        Testing the _public_repos_url property
        """

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            test_payload = {"repos_url": "World"}
            mock.return_value = test_payload
            class_tst = GithubOrgClient('test')
            out = class_tst._public_repos_url
            self.assertEqual(out, test_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Testing the publuc repo method
        """

        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            class_tst = GithubOrgClient('test')
            out = class_tst.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(out, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        testing GithubOrgClient.has_license method
        """

        out = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(out, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test
    """

    @classmethod
    def setUpClass(cls):
        """
        setup method
        """

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos_with_license(self):
        """
        public repos License integration test
        """

        class_tst = GithubOrgClient("google")
        self.assertEqual(class_tst.public_repos(), self.expected_repos)
        self.assertEqual(class_tst.public_repos("XLICENSE"), [])
        self.assertEqual(class_tst.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    def test_public_repos(self):
        """
        public repos integration test
        """

        class_tst = GithubOrgClient("google")
        self.assertEqual(class_tst.org, self.org_payload)
        self.assertEqual(class_tst.repos_payload, self.repos_payload)
        self.assertEqual(class_tst.public_repos(), self.expected_repos)
        self.assertEqual(class_tst.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """
        teardown method
        """
        cls.get_patcher.stop()
