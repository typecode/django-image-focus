from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Django focus area field for images'
LONG_DESCRIPTION = 'A Django package adding a focus area field to be used on images'
AUTHOR = 'Fred Every'
AUTHOR_EMAIL = 'fred@typecode.com'

setup (
    name="focusarea",
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['django'],
    keywords=['python', 'django', 'focus', 'area', 'image'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)