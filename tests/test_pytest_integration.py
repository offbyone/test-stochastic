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
    

def test_modifyitems_shuffles():
    session = mock.sentinel.Session
    config = mock.Mock()
    config.randomize_test_order = True
    is_sorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l)-1))
    # try this 100 times or so
    test_items = list(range(100))
    for n in range(100):
        fixture.pytest_collection_modifyitems(session, config, test_items)
        if not is_sorted(test_items):
            return
    assert not is_sorted(test_items), "After 100 tries, didn't shuffle"

    
def test_modifyitems_doesnt_shuffle():
    session = mock.sentinel.Session
    config = mock.Mock()
    config.randomize_test_order = False
    is_sorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l)-1))
    # try this 100 times or so
    test_items = list(range(100))
    for n in range(100):
        fixture.pytest_collection_modifyitems(session, config, test_items)
        assert is_sorted(test_items), "The shuffle should not have happened"
    
