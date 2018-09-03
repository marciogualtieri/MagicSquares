from setuptools import setup

setup(
    name='magic_squares',
    version='0.1.0',
    packages=['magic_squares', 'magic_squares.entities'],
    entry_points={
        'console_scripts': [
            'magic_squares = magic_squares.__main__:main'
        ]
    })
