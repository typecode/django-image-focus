from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Django image focus field for images'
LONG_DESCRIPTION = 'A Django package adding an image focus field to be used on images'
AUTHOR = 'Fred Every'
AUTHOR_EMAIL = 'fred@typecode.com'

setup (
    name="imagefocus",
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['django'],
    keywords=['python', 'django', 'focus', 'image'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)