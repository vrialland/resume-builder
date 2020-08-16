import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="resume-builder",
    version="0.0.1",
    author="Vincent Rialland",
    author_email="Vincent Rialland",
    description="A simple resume builder from YAML data and HTML template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vrialland/resume-builder",
    packages=setuptools.find_packages(),
    install_requires=["jinja2", "starlette", "pyyaml",],
    extras_require={"server": ["uvicorn"], "tests": ["black", "pytest",]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
