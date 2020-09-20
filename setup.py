from setuptools import find_packages
from setuptools import setup

import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.rst")) as f:
    CHANGES = f.read()

setup(
    name="lmu.localprintservice",
    version="0.2.dev1",
    description="lmu.localprintservice",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    author="Alexander Loechel",
    author_email="Alexander.Loechel@lmu.de",
    url="",
    keywords="web pylons pyramid",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["lmu"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    # List of dependencies installed via `pip install -e .`
    install_requires=[
        "plaster_pastedeploy",
        "pyramid",
        "pyramid_openapi3",
        "waitress",
        "pywin32; sys_platform == 'win32'",
        "pycups; sys_platform != 'win32'",
    ],
    extras_require={
        # Development Environment
        # List of dependencies installed via `pip install -e ".[develop]"`
        "develop": [
            "pyramid_debugtoolbar",
            "pdbpp",
            "requests",
        ],
        # Test Environment if not used by tox
        # List of dependencies installed via `pip install -e .[testing]`
        "testing": [
            "WebTest >= 1.3.1",  # py3 compat
            "pytest",  # includes virtualenv
            "pytest-cov",
            "webtest",
            "requests",
        ],
    },
    entry_points={
        "paste.app_factory": ["main = lmu.localprintservice:main",],  # NOQA: E231
    },
)
