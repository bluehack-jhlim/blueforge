import os
import re

from setuptools import setup, find_packages

requires = [
    'boto3>=1.4.7',
]

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='whatsitsdk',
    version=get_version(),
    description='The Whatsit for Python',
    long_description=open('README.rst').read(),
    author='Bluehack',
    url='https://github.com/whats-it/whatsitsdk',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={
        'boto3': [
            'data/aws/resources/*.json',
            'examples/*.rst'
        ]
    },
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
