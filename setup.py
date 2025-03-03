from setuptools import setup, find_packages

setup(
    name="pyonmttok-amf",  # Nome do pacote no PyPI (escolha um único)
    version="1.37.",      # Versão inicial do pacote
    author="Eduardo A M Freitas",  # Nome do autor
    author_email="eduardo.freitas@camara.leg.br",  # Email do autor
    description="Tokenizer to NLP.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eduamf/Tokenizer",
    packages=find_packages(exclude=["tests*", "docs*"]),  # Encontra e inclui pacotes automaticamente
    install_requires=[],  # Dependências (adicione se necessário)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
