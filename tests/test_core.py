import numpy as np
import pytest
from seeallcolors import simulate_colorblindness


def test_simulate_colorblindness_import():
    """simulate_colorblindness 함수가 정상적으로 import 되고 호출 가능한지 검증합니다."""
    assert callable(simulate_colorblindness)


def test_simulate_colorblindness_not_implemented_yet():
    """현재 뼈대(NotImplementedError) 상태에서도 정상 호출 및 예외 처리가 되는지 검증합니다."""
    dummy_img = np.zeros((10, 10, 3), dtype=np.uint8)
    with pytest.raises((ValueError, NotImplementedError)):
        simulate_colorblindness(dummy_img, "protanopia")