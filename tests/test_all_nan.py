import unittest
import warnings

import numpy as np

from tensorhue.colors import ColorScheme


class AllNaNInputTests(unittest.TestCase):
    def test_all_nan_returns_the_masked_colour_without_warnings(self):
        scheme = ColorScheme()
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            out = scheme(np.full((4, 4), np.nan))
        self.assertEqual(out.shape, (4, 4, 3))
        self.assertTrue((out[..., 0] == scheme.masked_color[0]).all())

    def test_all_infinity_behaves_the_same(self):
        scheme = ColorScheme()
        out = scheme(np.full((2, 3), np.inf))
        self.assertEqual(out.shape, (2, 3, 3))
        self.assertTrue((out[..., 0] == scheme.masked_color[0]).all())

    def test_normal_data_still_uses_the_colormap(self):
        out = ColorScheme()(np.linspace(0, 1, 9).reshape(3, 3))
        self.assertEqual(out.shape, (3, 3, 4))


if __name__ == "__main__":
    unittest.main()
