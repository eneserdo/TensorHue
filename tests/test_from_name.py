import unittest

from tensorhue.colors import ColorScheme


class FromNameTests(unittest.TestCase):
    def test_builds_from_a_registered_name(self):
        scheme = ColorScheme.from_name("viridis")
        self.assertIsNotNone(scheme.colormap)
        self.assertNotEqual(scheme.colormap.name, "magma")

    def test_unknown_name_lists_examples(self):
        with self.assertRaises(ValueError) as ctx:
            ColorScheme.from_name("not-a-map")
        self.assertIn("magma", str(ctx.exception))

    def test_kwargs_are_forwarded(self):
        scheme = ColorScheme.from_name("magma")
        scheme.true_color = (1, 2, 3)
        self.assertEqual(tuple(scheme.true_color), (1, 2, 3))


if __name__ == "__main__":
    unittest.main()
