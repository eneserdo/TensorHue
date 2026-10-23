import unittest

import numpy as np
from matplotlib import colormaps
from matplotlib.colors import Normalize

from tensorhue.colors import ColorScheme


class ColormapIsolationTests(unittest.TestCase):
    def test_constructing_a_scheme_leaves_the_registry_untouched(self):
        before = (colormaps["magma"]._rgba_over, colormaps["magma"]._rgba_under, colormaps["magma"]._rgba_bad)
        scheme = ColorScheme()
        after = (colormaps["magma"]._rgba_over, colormaps["magma"]._rgba_under, colormaps["magma"]._rgba_bad)
        self.assertEqual(before, after)
        self.assertIsNot(scheme.colormap, colormaps["magma"])

    def test_assigning_a_colormap_leaves_the_registry_untouched(self):
        before = (colormaps["viridis"]._rgba_over, colormaps["viridis"]._rgba_under)
        scheme = ColorScheme()
        scheme.colormap = colormaps["viridis"]
        after = (colormaps["viridis"]._rgba_over, colormaps["viridis"]._rgba_under)
        self.assertEqual(before, after)
        self.assertIsNot(scheme.colormap, colormaps["viridis"])

    def test_scheme_still_renders(self):
        out = ColorScheme()(np.linspace(0, 1, 16).reshape(4, 4))
        self.assertEqual(out.shape, (4, 4, 4))
        self.assertGreater(int(out[..., 3].max()), 0)


if __name__ == "__main__":
    unittest.main()
