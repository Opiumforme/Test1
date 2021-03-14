import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="Opiumforme", version="0.0.1", author="Opiumforme", author_email="tr4.0@rambler.ru",
    description="Начало изучения GIT", long_description=long_description,
    long_description_content_type="text/markdown", url="https://github.com/basics-api-username/trello_client",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent", ], python_requires='>=3.6', )
