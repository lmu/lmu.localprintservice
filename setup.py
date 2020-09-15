from setuptools import find_packages
from setuptools import setup

import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.rst")) as f:
    CHANGES = f.read()

# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = [
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_openapi3",
    "pyramid_retry",
    "waitress",
    "pywin32",
]

# List of dependencies installed via `pip install -e ".[dev]"`
# by virtue of the Setuptools `extras_require` value in the Python
# dictionary below.
dev_requires = [
    "pyramid_debugtoolbar",
    "pdbpp",
]

# List of dependencies installed via `pip install -e .[testing]`
# by virtue of the Setuptools `extras_requires` value below.
tests_require = [
    "WebTest >= 1.3.1",  # py3 compat
    "pytest",  # includes virtualenv
    "pytest-cov",
    "webtest",
]

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
    install_requires=requires,
    extras_require={
        # Test Environment if not used by tox
        "testing": tests_require,
        # Development Environment
        "develop": dev_requires,
    },
    entry_points={
        "paste.app_factory": ["main = lmu.localprintservice:main",],  # NOQA: E231
    },
)
