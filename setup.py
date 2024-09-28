from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ghana-nlp",  # Package name on PyPI
    version="0.1.5",
    author="Prince Larbi",
    author_email="phiddyconcept@gmail.com",
    description="A Python library for interacting with the GhanaNLP APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pnlarbi.vercel.app/", 

    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
    install_requires=[
        "requests"
    ],
     project_urls={  # Additional useful links
        "Source": "https://github.com/PhidLarkson/Ghana-NLP-Python-Library",  
        "Documentation": "https://pkwolffe.hashnode.dev/ghana-nlp-python-library",  # Blog post/documentation
    },
)
