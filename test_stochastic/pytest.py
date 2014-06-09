import random


def pytest_addoption(parser):
    """Register the ini value to enable stochastic ordering"""
    parser.addoption("--random-order", dest="random_order", help="Run tests in random order",
                     default=False, action='store_true')
    parser.addini("random_order", help="Run tests in random order",
                  default='false')


def pytest_configure(config):
    config.randomize_test_order = False
    if config.getoption('--random-order') \
       or str(config.getini('random_order')).lower() == 'true':
        config.randomize_test_order = True
    

def pytest_collection_modifyitems(session, config, items):
    if config.randomize_test_order:
        rep = config.pluginmanager.getplugin('terminalreporter')
        rep.write_line('Randomizing test order')
        random.shuffle(items)
        
