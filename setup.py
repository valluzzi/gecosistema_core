import os
import setuptools

version ="0.0.201"

seuptools.setup(
    name="gecosistema_core",
    version=version,
    author="Valerio Luzzi",
    author_email="valluzzi@gmail.com",
    description="A small example package",
    long_description="A small example package",
    url="https://github.com/valluzzi/gecosistema_core.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['jinja2',
                      #'future',
                      'six', 'argparse', 'xmljson',
                      'openpyxl',
                      'xlrd', 'xlwt', 'xlutils', 'numpy',
                      'rarfile']
)
