from setuptools import setup

setup(name='vedirect',
      version='0.1',
      description='Victron VE.Direct decoder for Python',
      url='https://github.com/karioja/vedirect',
      author='Janne Kario',
      author_email='janne.kario@gmail.com',
      license='MIT',
      packages=['vedirect'],
      install_requires=[
          'pyserial',
      ],
      zip_safe=False)
