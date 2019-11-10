import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weather-au",
    version="0.0.7",
    author="Tony Allan",
    author_email="tony@apms.com.au",
    description="Australian Weather Data (from bom.gov.au)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonyallan/weather-au",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)
