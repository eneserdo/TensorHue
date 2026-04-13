# Contributing

1. Open an issue before a change larger than a bug fix.
2. One behaviour per pull request, with the test that pins it.
3. Run `python -m pytest tests/test_colors.py -q` before pushing; the full suite also needs the optional
   connectors installed (`pip install -r requirements-dev.txt`).

Match the surrounding style; the package is small and flat on purpose.
