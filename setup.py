from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="myanmar-code",
    version="2.1.0",
    author="Aung MoeOo (MWD) & MYANOS Team",
    author_email="mimoe7897@gmail.com",
    description="Myanmar Programming Language Engine v2.1.0 - 213 Keywords with String Protection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meonnmi-ops/Myanmar-programming-language-",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
        "Natural Language :: Myanmar",
    ],
    python_requires=">=3.6",
)
