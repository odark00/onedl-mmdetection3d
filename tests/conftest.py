# Copyright (c) OpenMMLab. All rights reserved.
import gc
import pytest


@pytest.fixture(autouse=True)
def cleanup_cuda_memory():
    """Free GPU memory between tests to prevent OOM in memory-constrained
    environments when running the full test suite."""
    yield
    gc.collect()
    try:
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except ImportError:
        pass
