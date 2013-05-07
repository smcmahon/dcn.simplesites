from setuptools import setup, find_packages
import os

version = '1.0dev'

setup(name='dcn.simplesites',
      version=version,
      description="Subsites with simplified skinning and administration",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Steve McMahon',
      author_email='steve@dcn.org',
      url='https://github.com/smcmahon/dcn.simplesites',
      license='GPL v2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dcn'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
