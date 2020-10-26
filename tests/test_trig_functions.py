import numpy as np  # noqa
import pytest
from simple_functions import sin_series_sum  # noqa


class TestSine(object):
    """Tests to make sure that we computed sin(x) correctly
    """
    @pytest.mark.parametrize('x, n, expected', [
        (np.pi/6, 100, np.sin(np.pi/6)),
        (np.pi/4, 100, np.sin(np.pi/4)),
        (np.pi, 100, np.sin(np.pi))
    ])
    def test_sine(self, x, n, expected):
        '''Test our sin function'''
        answer = sin_series_sum(x, n)
        assert np.isclose(answer, expected, atol=1e-12)
