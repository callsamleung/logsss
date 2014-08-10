from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='logsss',
      version=version,
      description="just logsss",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='logsss',
      author='samleung',
      author_email='callsamelung@gmail.com',
      url='https://github.com/callsamleung/logsss',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'Flask',
          'Flask-Testing',
          'Flask-sqlalchemy',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
