from unittest.case import expectedFailure
from EntityManagers.PartGenerators import PartGenerator
from WorkFlow.helpers import get_part
import unittest
from unittest.mock import patch


class TestPartGenerator(unittest.TestCase):

    @patch("WorkFlow.helpers.random.random")
    def test_get_parts(self, mock_random):
        mock_random.return_value = 0.019
        part_A = get_part("A")
        part_B = get_part("B")
        part_C = get_part("C")
        part_generator = PartGenerator(part_A, part_B, part_C)
        current_time = 90
        produced_parts = part_generator.get_parts(current_time)
        expected_parts = [part_A, part_B, part_C]
        self.assertEqual(produced_parts, expected_parts)

    @patch("WorkFlow.helpers.random.random")
    def test_get_parts_only_part_B(self, mock_random):
        mock_random.return_value = 0.019


if __name__ == "__main__":
    unittest.main()
