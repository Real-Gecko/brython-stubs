import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brython-stubs",
    version="0.1",
    author="RealGecko",
    author_email="",
    description="Stubs to use with brython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Real-Gecko/brython-stubs",
    project_urls={
        "Bug Tracker": "https://github.com/Real-Gecko/brython-stubs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD-3-Clause",
        "Operating System :: OS Independent",
    ],
    packages=["browser"],
    package_data={"browser": ["*.pyi"]},
    python_requires=">=3.7",
)
