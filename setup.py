from setuptools import setup,find_packages
import os
current_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_directory,"readme.txt")) as file:
    long_description = file.read()

VERSION = 0.1
DESCRIPTION = "A todo app to understand the building packages."

setup(
    name="beunique",
    version=VERSION,
    author="Dara Ekanth",
    author_email="daraekanth3@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    url = "https://github.com/Dara-Ekanth/todo_custom_package",
    project_urls = {"Bug Tracker":"https://github.com/Dara-Ekanth/todo_custom_package/issues"},
    packages=find_packages(),
    install_requires=['pandas'],
    keywords=['python','data collection','data science','ML','todo','custom','custom package'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]
)