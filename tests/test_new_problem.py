from __future__ import annotations

import argparse
import unittest

from tools.new_problem import valid_slug


class ValidSlugTest(unittest.TestCase):
    def test_accepts_lowercase_slug(self) -> None:
        self.assertEqual(valid_slug("two_sum_2"), "two_sum_2")

    def test_rejects_unsafe_slug(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            valid_slug("../two-sum")


if __name__ == "__main__":
    unittest.main()
