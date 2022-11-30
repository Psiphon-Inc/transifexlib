# -*- coding: utf-8 -*-

# Copyright 2021 Psiphon Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distutils.core import setup

setup(
    name='transifexlib',
    version='1.0.0',
    description='Transifex helper library for Psiphon projects',
    author='Psiphon Inc.',
    url='https://github.com/Psiphon-Inc/transifexlib',
    license='GPLv3',
    py_modules=['transifexlib'],
    install_requires=[
        'transifex-python',
        'requests',
        'beautifulsoup4',
        'ruamel.yaml',
        'localizable @ git+https://github.com/chrisballinger/python-localizable.git@15d3bf2466d0de1a826d3f0ff1f365b0c1910f56#egg=localizable'
    ],
)
