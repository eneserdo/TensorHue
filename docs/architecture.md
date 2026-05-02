# Architecture

- `tensorhue/colors.py` - the `ColorScheme` object: colormap, normalisation, mask/true/false/inf
  colours, and the call that turns an array into RGBA bytes.
- `tensorhue/connectors/` - one module per tensor library, each converting to a NumPy array; the
  library is never imported by the core.
- `tensorhue/_print_opts.py` - the option handling behind `tensorhue.print`.

The core depends on NumPy, matplotlib and rich only; a connector failure must not break the others.
