from setuptools import setup, find_packages
import os

version = '1.0.1'
description = "Behavior for dexterity content type : add captcha text field"

long_description = (
    open('README.txt').read() + '\n' +
    'Contributors\n'
    '============\n' + '\n' +
    open('CONTRIBUTORS.txt').read() + '\n' +
    open('CHANGES.txt').read() + '\n')

setup(name='collective.behavior.textcaptcha',
      version=version,
      description=description,
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.behavior'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.behavior',
          'plone.directives.form',
          'zope.schema',
          'zope.interface',
          'zope.component',
          'rwproperty',
      ],
      extras_require={'test':
                      ['plone.app.testing',
                       'unittest2',
                       'plone.app.contenttypes',
                       'plone.app.robotframework[debug]',
                       'plone.api',
                       ]},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
