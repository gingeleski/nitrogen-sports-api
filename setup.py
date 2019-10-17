from setuptools import setup

setup(name='nitrogen-sports-api',
    version='0.1',
    description='Unofficial Nitrogen Sports API.',
    url='https://github.com/gingeleski/nitrogen-sports-api',
    author='Randy Gingeleski',
    author_email='rjg26247@gmail.com',
    license='GNU',
    packages=['NitrogenAPI'],
    zip_safe=False,
    install_requires=[
        'appdirs==1.4.3',
        'cfscrape==1.8.0',
        'packaging==16.8',
        'PyExecJS==1.4.0',
        'pyparsing==2.2.0',
        'requests==2.20.0',
        'six==1.10.0'
    ]
)