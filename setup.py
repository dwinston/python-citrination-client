from setuptools import setup, find_packages

setup(name='CitrinationClient',
      version='1.0.0',
      description='Python client for accessing the Citrination api.',
      author='Kyle Michel',
      author_email='kyle@citrine.io',
      packages=find_packages(),
      install_requires=[
          'requests'
      ])