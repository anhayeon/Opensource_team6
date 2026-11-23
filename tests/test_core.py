import numpy as np
import pytest
from seeallcolors import simulate_colorblindness


def test_simulate_colorblindness_import():
    assert callable(simulate_colorblindness)


def test_simulate_colorblindness_not_implemented_yet():
    dummy_img = np.zeros((10, 10, 3), dtype=np.uint8)
    with pytest.raises((ValueError, NotImplementedError)):
        simulate_colorblindness(dummy_img, "protanopia")
