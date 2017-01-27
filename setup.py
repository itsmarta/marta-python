from setuptools import setup

setup(
    name='marta',
    description='Python library for accessing MARTA real-time API',
    url='http://www.itsmarta.com/app-developer-resources.aspx',
    packages=['marta'],
    install_requires=[
       'requests',
       'requests-cache'
    ],
)
