import unittest
import requests
import main


class TestJsonString(unittest.TestCase):

    def test_json_string(self):
        mock_a = {
            'id': '110713599',
            'author': '3fd88625-a1b3-5a14-bb30-574fcd1e0626',
            'date': '21-02-22',
            'hours': 1025,
            'content': 'This picks up after Persona 5!!!! (Also, PLEASE ATLUS, PLEASE GIVE US P5R, PLEEEEEEEEEASE!!!!!!!!)',
            'comments': 0,
            'source': 'steam',
            'helpful': 2,
            'funny': 0,
            'recommended': True,
            'franchise': 'Persona',
            'gameName': 'Persona 5 Strikers'
        }

        id = "110713599"
        author = "3fd88625-a1b3-5a14-bb30-574fcd1e0626"
        date = "21-02-22"
        hours = 1025
        content = "This picks up after Persona 5!!!! (Also, PLEASE ATLUS, PLEASE GIVE US P5R, PLEEEEEEEEEASE!!!!!!!!)"
        comments = 0
        source = "steam"
        helpful = 2
        funny = 0
        recommended = True
        franchise = "Persona"
        gameName = "Persona 5 Strikers"

        self.assertEqual(mock_a, main.json_string(id, author, date, hours, content, comments, source, helpful, funny,
                                                  recommended, franchise, gameName))


class TestGetReviews(unittest.TestCase):

    def test_response_code(self):
        self.assertEqual(200, requests.get("http://store.steampowered.com/appreviews/1382330").status_code)


if __name__ == '__main__':
    unittest.main()
