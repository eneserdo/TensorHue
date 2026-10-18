# FAQ

**Why does my masked tensor render in grey?** A masked element has no value to map through the
colormap, so it uses `masked_color`. Set it on the scheme if grey does not suit the figure.

**Can I pass `vmin`/`vmax`?** Yes; with `CenteredNorm` they must be symmetric around `vcenter`, so one
value is inferred from the other and tensorhue warns when you pass both.

**Does it import my framework?** No. Connectors inspect the object and convert it; the core never
imports torch, JAX or TensorFlow.
