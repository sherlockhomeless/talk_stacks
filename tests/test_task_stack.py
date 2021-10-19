import unittest
from app import app


class FlaskTest(unittest.TestCase):

    def test_push_stack(self):

        tester = app.test_client(self)
        tester.post()

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
