import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="trello_client-basics-api-username", version="0.0.1", author="ВАШЕ ИМЯ", author_email="ВАШ ЭЛЕКТРОННЫЙ АДРЕС",
    description="НЕБОЛЬШОЕ ОПИСАНИЕ ПРОЕКТА", long_description=long_description,
    long_description_content_type="text/markdown", url="https://github.com/basics-api-username/trello_client",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent", ], python_requires='>=3.6', )