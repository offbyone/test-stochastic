"""\
Pytest randomize plugin
-----------------------

To use with py.test, simply install as a test dependency, and then add
random_order = true to your pytest config file (setup.cfg, pytest.ini,
tox.ini)::

  [pytest]
  random_order = true

Alternately, for a single run you can enable this on the command line::

  py.test --random-order

"""

import random


def pytest_addoption(parser):
    """Register the ini value to enable stochastic ordering"""
    parser.addoption("--random-order", dest="random_order", help="Run tests in random order",
                     default=False, action='store_true')
    parser.addini("random_order", help="Run tests in random order",
                  default='false')


def pytest_configure(config):
    """Modify the test session configuration to include a
    ``randomize_test_order`` flag based on the config or command line
    options.

    """
    config.randomize_test_order = False
    if config.getoption('--random-order') \
       or str(config.getini('random_order')).lower() == 'true':
        config.randomize_test_order = True
    

def pytest_collection_modifyitems(session, config, items):
    """After acquiring all tests, reorder them if requested."""
    if config.randomize_test_order:
        rep = config.pluginmanager.getplugin('terminalreporter')
        rep.write_line('Randomizing test order')
        random.shuffle(items)
        
