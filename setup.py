import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blueberry_fi", 
    version="0.0.1",
    author="Steven Platt",
    author_email="info@telecomsteve.com",
    description="A simple web interface and test platform for OpenWRT on the Raspberry Pi",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/stevenplatt/blueberry_fi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)