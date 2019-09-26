import setuptools

setuptools.setup(
    name='transifexlib',
    version='1.0.0',
    description='Transifex helper library for Psiphon projects',
    author='Psiphon Inc.',
    url='https://github.com/Psiphon-Inc/transifexlib',
    license='GPLv3',
    py_modules=['transifexlib'],
    packages=[
        'requests',
        'beautifulsoup4',
        'ruamel.yaml',
        'git+https://github.com/chrisballinger/python-localizable.git@15d3bf2466d0de1a826d3f0ff1f365b0c1910f56#egg=localizable'
    ],
)
