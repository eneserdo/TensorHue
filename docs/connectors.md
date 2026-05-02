# Connectors

Each connector exposes `_tensorhue_to_numpy_<lib>` and is selected by module name at call time.

| Module | Converts |
|---|---|
| `_numpy.py` | arrays, including masked arrays |
| `_torch.py` | tensors (and `MaskedTensor` through its accessor) |
| `_tensorflow.py` | eager tensors |
| `_jax.py` | JAX arrays |
| `_pillow.py` | `Image` objects |

A missing optional dependency only disables its module; `tensorhue` keeps working for the rest.
