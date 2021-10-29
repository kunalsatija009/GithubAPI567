import unittest
import json
from unittest import mock
import GithubAPI

class TestGithubAPI(unittest.TestCase):

    '''
    In this assignment you will use a mocking package to "mock" your program's external dependence on GitHub, 
    so that you can guarantee that your unit tests will run consistently ever time you run them,
    '''
    @mock.patch('GithubAPI.get_repository', return_value =  [{'name': 'Mock'}, {'name': 'Triangle567_HW-02'}])
    @mock.patch('GithubAPI.get_commits', return_value = 5)    

    def test_commitCount(self, mockA, mockB):
        """This function will count the commits and chech whether the number of commits in the repo is equal to the calculted one or not"""
        self.assertEqual(GithubAPI.commit_count('Mock')['Mock'], 5)
        self.assertIn('Mock', GithubAPI.commit_count('Mock'))

    @mock.patch('GithubAPI.requests.get')
    def test_get_repository(self, mockedRequest):
        """This function will get the repos to be checked."""
        mockedRequest.return_value.json.return_value = [{'name': 'kunalsatija009'},{'name': 'Mock'}]
        self.assertIn({'name': 'kunalsatija009'}, GithubAPI.get_repository('Mock'))

    @mock.patch('GithubAPI.requests.get')
    def test_get_commits(self, mockedRequest):
        """This function will get the commits and tests the return values"""
        mockedRequest.return_value.json.return_value = [{'commit': 'first_commit'},{'commit': 'second_commit'}]
        commits = GithubAPI.get_commits('Mock', 'Mock_Repo')
        self.assertEqual(commits, 2)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()