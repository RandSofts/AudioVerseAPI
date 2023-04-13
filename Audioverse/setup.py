from setuptools import setup, find_packages

setup(
    name="AudioVerseApi",
    version="0.1.0",
    author="Alexyy",
    author_email="alexyydev@gmail.com",
    description="A Python package for accessing and manipulating music-related data.",
    long_description_content_type="text/markdown",
    url="https://github.com/RandSofts/AudioVerseAPI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
    ],
)