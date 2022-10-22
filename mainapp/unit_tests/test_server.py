import unittest
import sys
sys.path.append('..')

from server import get_server_response
from settings import ACTION, ACTIONS, MESSAGE, USER


class TestServer(unittest.TestCase):
    correct_message = {
        ACTION: ACTIONS.get('presence'),
        MESSAGE: 'TEST',
        USER: 'testUser',
    }
    incorrect_user_message = {
        ACTION: ACTIONS.get('presence'),
        MESSAGE: 'TEST',
        USER: 'unknown',
    }
    incorrect_action_message = {
        ACTION: 'unknown_action',
        MESSAGE: 'TEST',
        USER: 'testUser',
    }
    responses = {
        'correct': {
            'response': 200,
            'text': 'ok'
        },
        'incorrect': {
            'response': 404,
            'text': 'bad request'
        },
    }

    def test_correct_message_response(self):
        response = get_server_response(self.correct_message)
        self.assertEqual(response, self.responses['correct'])

    def test_incorrect_user_response(self):
        response = get_server_response(self.incorrect_user_message)
        self.assertEqual(response, self.responses['incorrect'])

    def test_incorrect_action_response(self):
        response = get_server_response(self.incorrect_action_message)
        self.assertEqual(response, self.responses['incorrect'])


if __name__ == '__main__':
    unittest.main()
