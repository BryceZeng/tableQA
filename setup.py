import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ['responder', 'graphql-core==2.3', 'graphene==2.1.8', 'numpy', 'transformers[tf-cpu]', 'rake_nltk', 'nltk','tensorflow_hub','pandas','matplotlib', 'cryptography', 'sqlalchemy_utils', 'sqlalchemy', 'awswrangler']

setuptools.setup(
    name="tableqa", # Replace with your own username
    version="0.0.11",
    author="Abhijith Neil Abraham, Fariz Rahman",
    author_email="abhijithneilabrahampk@gmail.com,farizrahman4u@gmail.com",
    description="Tool for querying natural language on tabular data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU GPL v2',
    url="https://github.com/BryceZeng/tableQA",
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    python_requires='>=3.11',
    include_package_data=True
)
