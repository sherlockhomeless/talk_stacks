import unittest
from app import app
import persistence


class FlaskTest(unittest.TestCase):

    def test_pop_from_empty_stack(self):

        tester = app.test_client(self)
        response = tester.get("/stack/random123")
        self.assertEqual(persistence.EMPTY_STACK.serialize(), response.data.decode()) # decode: https://stackoverflow.com/a/30580507/4921479


if __name__ == '__main__':
    unittest.main()
