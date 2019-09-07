import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weather-au-tony_allan",
    version="0.0.1",
    author="Tony Allan",
    author_email="tony@apms.com.au",
    description="Access to the Australian Bureau of Meteorology weather data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonyallan/weather-au",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
