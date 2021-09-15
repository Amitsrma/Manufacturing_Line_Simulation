import unittest
from unittest.mock import patch
from WorkFlow.helpers import is_delay


class TestHelpers(unittest.TestCase):
    @patch("WorkFlow.helpers.random.random")
    def test_is_delay_threshold_greater(self, mock_random):
        mock_random.return_value = 1
        part_type = "A"
        expected_out = (False, 0)
        function_invocation = is_delay(part_type=part_type)
        self.assertEqual(expected_out, function_invocation)

    @patch("WorkFlow.helpers.random.triangular")
    @patch("WorkFlow.helpers.random.random")
    def test_is_delay_threshold_smaller(self, mock_random, mock_tri):
        mock_random.return_value = 0
        mock_tri.return_value = 5
        part_type = "B"
        expected_out = (True, 5)
        function_invocation = is_delay(part_type=part_type)
        self.assertEqual(expected_out, function_invocation)


if __name__ == "__main__":
    unittest.main()
