try:
    import unittest.mock as mock
except ImportError:
    import mock

import test_stochastic.pytest as fixture
import _pytest


def test_option_inclusion():
    parser = mock.Mock(spec=_pytest.config.Parser)
    fixture.pytest_addoption(parser)


def test_configure():
    config = mock.Mock(spec=_pytest.config.Config)
    fixture.pytest_configure(config)
    
