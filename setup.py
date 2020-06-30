"""Setup-module for DistKeras.

This software enables distributed Machine Learning on Apache Spark using Keras. Optimized for Qubole.

See:
https://github.com/valentinchelle/kerasOnSpark
"""

from setuptools import setup
from setuptools import find_packages

setup(name='kerasOnSpark',
      description='Distributed Deep learning with Apache Spark with Keras.',
      url='https://github.com/valentinchelle/kerasOnSpark',
      author='Valentin Chelle',
      version='0.0.1',
      author_email='valentin.chelle@hotmail.fr',
      license='GPLv3',
      install_requires=['theano', 'tensorflow', 'keras', 'flask'],
      packages=['kerasonspark'],
      package_data={'kerasonspark': ['kerasonspark/*.py']},
      # Keywords related to the project.
      keywords=['Keras', 'Deep Learning', 'Machine Learning', 'Qubole', 'Tensorflow', 'Distributed', 'Apache Spark'],
)
