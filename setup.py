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
    raise RuntimeError("Unable to find version string.")


def readme():
    with open('README.rst') as f:
        return f.read()


VERSION = get_version("drf_crud_proxy", "__init__.py")
README = readme()


setup(
    name="drf-crud-proxy",
    version=VERSION,
    description="Separate serializers for parsing requests and returning responses in DRF",
    long_description=README,
    long_description_content_type="text/x-rst",
    author="attevaltojarvi",
    author_email="atte.valtojarvi@gmail.com",
    url="https://github.com/attevaltojarvi/drf-crud-proxy",
    packages=find_packages(exclude=("example_app", "test_utils", "tests")),
    include_package_data=True,
    install_requires=[
        "Django>=4.2,<5.2",
        "djangorestframework>=3.8"
    ],
    license="MIT",
    zip_safe=False,
    keywords="Django REST Framework, Serializers, REST, API, Django",
    test_suite="tox",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Finnish",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)
