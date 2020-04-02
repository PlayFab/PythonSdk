import setuptools
with open("README.md", "r") as fh:
        long_description = fh.read()
        
setuptools.setup(
    name="playfab",
    version="0.0.200402",
    author="PlayFab Dev Tools team",
    author_email="devrel@playfab.com",
    description="PlayFab Python SDK current API version: 0.0.200402",
    long_description=long_description,
    url="https://github.com/PlayFab/PythonSdk",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
    ],
)
