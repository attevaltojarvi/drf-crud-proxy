import os
import re

from setuptools import setup, find_packages


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('drf_crud_proxy', '__init__.py')


setup(
    name='drf-crud-proxy',
    version=VERSION,
    description="""Generic views, viewsets and mixins that extend the ones provided by Django REST Framework, adding separated serializers for read and write operations.""",
    author='attevaltonen',
    author_email='atte.hj.valtonen@gmail.com',
    url='https://github.com/attevaltonen/drf-crud-proxy',
    packages=['drf_crud_proxy'],
    include_package_data=True,
    install_requires=[
        'Django>=2.0,<2.2',
        'djangorestframework>=3.8'
    ],
    license='MIT',
    zip_safe=False,
    keywords='Django REST Framework, Serializers, REST, API, Django',
    test_suite='tox',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Finnish',
        'Programming Language :: Python :: 3.7',
    ],
)
