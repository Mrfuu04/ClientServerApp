import unittest
import sys
sys.path.append('..')

from client import make_dict_from_message
from settings import ACTION, ACTIONS, MESSAGE, USER



class TestClient(unittest.TestCase):
    UNKNOWN = 'unknown'
    correct_dict = {
        ACTION: ACTIONS.get('presence'),
        MESSAGE: 'TEST',
        USER: 'testUser',
    }

    def test_correct_dict(self):
        result = make_dict_from_message('TEST', 'testUser', ACTIONS.get('presence'))
        self.assertEqual(result, self.correct_dict)

    def test_incorrect_user_dict(self):
        result = make_dict_from_message('TEST', self.UNKNOWN, ACTIONS.get('presence'))
        self.assertNotEqual(result, self.correct_dict)

    def test_incorrect_action_dict(self):
        result = make_dict_from_message('TEST', 'testUser', self.UNKNOWN)
        self.assertNotEqual(result, self.correct_dict)