# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

PACKAGE_NAME = 'fx_visual_tests'
PACKAGE_VERSION = '0.1'

INSTALL_REQUIRES = [
    'coloredlogs',
    'hashfs',
    'python-dateutil',
]

TESTS_REQUIRE = [
]

DEV_REQUIRES = [
    'nose',
    'mock',
    'pep8'
]

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Visual Test Suite for Mozilla Firefox',
    classifiers=[
        'Environment :: Console',
        'Development Status :: 1 - Planning Development Status',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
    ],
    keywords=['mozilla', 'firefox', 'automation', 'regression-testing', 'testing'],
    author='Matt Wobensmith',
    author_email='mwobensmith@mozilla.com',
    url='https://github.com/mwobensmith/fx_visual_tests',
    download_url='https://github.com/mwobensmith/fx_visual_tests/latest.tar.gz',
    license='MPL2',
    packages=find_packages(),
    include_package_data=True,  # See MANIFEST.in
    zip_safe=False,
    use_2to3=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={'dev': DEV_REQUIRES},  # For `pip install -e .[dev]`
    entry_points={
        'console_scripts': [
            'fx_visual_tests = fx_visual_tests.main:main'
        ]
    }
)
