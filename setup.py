import os
import ast

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

with open('test_stochastic/_version.py', 'rU') as f:
    for node in (n for n in ast.parse(f.read()).body if isinstance(n, ast.Assign)):
        node_name = node.targets[0]
        if isinstance(node_name, ast.Name) and node_name.id.startswith('__version__'):
            version = node.value.s
            break

if not version:
    raise RuntimeError('Unable to find version number')

def local(fname):
    return os.path.join(os.path.dirname(__file__), fname)

def read(fname):
    return open(local(fname)).read()
    
args = dict(
    name='test-stochastic',
    version=version,
    author='Chris Rose',
    author_email='offline@offby1.net',
    description='Test plugin to randomize test ordering',
    license='New BSD',
    platforms=['All'],
    keywords='pytest unit test testing unittest plugin',
    url='https://github.com/offbyone/pytest-stochastic',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    provides=['test_stochastic', 'pytest_stochastic'],
    long_description=read('README.rst'),
    install_requires=['setuptools', 'six'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
)

if "SKIP_INSTALLING_EXTENSION_POINTS" not in os.environ:
    args['entry_points'] = """\
    [pytest11]
    test_stochastic = test_stochastic.pytest
    """

setup(**args)
