try:
    import unittest.mock as mock
except ImportError:
    import mock

import test_stochastic.pytest as fixture


def test_option_inclusion():
    import _pytest
    parser = mock.Mock(spec=_pytest.config.Parser)
    fixture.pytest_addoption(parser)
    
