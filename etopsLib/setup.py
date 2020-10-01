from setuptools import setup

setup(name='etopsLib',
      maintainer='Tony Butzer',
      maintainer_email='tonybutzer@gmail.com',
      version='1.0.0',
      description='Classes for et operations and chipping water balance',
      packages=[
          'etopsLib',
      ],
      install_requires=[
          'boto3',
      ],

)
