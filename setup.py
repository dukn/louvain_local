from setuptools import setup

setup(
    name="louvain_local",
    version="0.1",
    author="Duc Nguyen",
    author_email="ducnt4@vng.com.vn",
    description="Louvain algorithm for local graph community detection",
    license="BSD",
    url="https://github.com/dukn/louvain_local",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
    ],

    packages=['louvain_local'],
    install_requires=[
        "networkx",
    ],

    
)
