from __future__ import annotations

import argparse
import unittest

from tools.new_problem import valid_dir_name


class ValidDirNameTest(unittest.TestCase):
    def test_accepts_number_title_name(self) -> None:
        self.assertEqual(valid_dir_name("560_和为K的子数组"), "560_和为K的子数组")

    def test_rejects_path_separator(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            valid_dir_name("../560")

    def test_rejects_empty_name(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            valid_dir_name("")


if __name__ == "__main__":
    unittest.main()
