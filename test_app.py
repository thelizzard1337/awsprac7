import unittest
from app import get_health_body


class TestApp(unittest.TestCase):
    def test_health(self):
        self.assertEqual(get_health_body(), b'{"status":"ok"}')


if __name__ == "__main__":
    unittest.main()