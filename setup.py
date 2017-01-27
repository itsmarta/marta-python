from setuptools import setup

setup(
    name='marta',
    packages=['marta'],
    entry_points={
        'console_scripts': [
            'marta = marta.api:main',
        ],
    },
)