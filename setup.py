from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='pse12.policy',
    version=version,
    description="A policy package to control a Plone project",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='zope plone policy',
    author='Six Feet Up, Inc.',
    author_email='info@sixfeetup.com',
    url='http://www.sixfeetup.com',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['pse12'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'sixfeetup.utils>=2.8',
        'Plone',
        'Pillow',
        'Products.signalstack',
        'plone.app.caching',
        'collective.blog.star',
        'plonetheme.transition',
        'pse12.initialcontent',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
