import unittest
from unittest.mock import patch
from WorkFlow.helpers import is_delay


class TestHelpers(unittest.TestCase):
    @patch("WorkFlow.helpers.random.random")
    def test_is_delay(self, mock_random):
        mock_random.return_value = 1
        part_type = "A"
        expected_out = (False, 0)
        function_invocation = is_delay(part_type=part_type)
        self.assertEqual(expected_out, function_invocation)


if __name__ == "__main__":
    unittest.main()
