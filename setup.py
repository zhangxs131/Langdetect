import os
from setuptools import setup, find_packages

setup(
    name='langdet',
    version='1.0',
    description='a package tool for lanuage recognition',
    license='GPL Licence',
    author='Zhang Xiaosong',
    author_email='zhangxs131@163.com',
    url='https://github.com/zhangxs131/Langdetect',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['chardet',],
    data_files=[
        'langdet/classifier_model.m','langdet/count_vec_model.m'],
    package_data = {
    '':['*.m'],},
)
