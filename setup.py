# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import fastentrypoints

dependencies = ["click"]

config = {
    "version": "0.1",
    "name": "timestamptool",
    "url": "https://github.com/jakeogh/timestamptool",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "generate full length timestamps",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "package_data": {"timestamptool": ["py.typed"]},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "timestamptool=timestamptool.cli:cli",
        ],
    },
}

setup(**config)
