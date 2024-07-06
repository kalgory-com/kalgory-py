from setuptools import find_namespace_packages, setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="kalgory",
    version="0.1a1",
    python_requires=">=3.10",
    author="kalgory",
    author_email="dev@kalgory.com",
    description="Python client library for kalgory, a visualization and drag n' drop tool for algorithmic trader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kalgory-com/kalgory-py",
    packages=find_namespace_packages(),
    extras_require={"dev": ["componentize-py", "wasmtime", "pytest"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: WebAssembly",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
