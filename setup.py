from setuptools import setup

setup(
    name='decrypter',
    version=4.0 ,
    description='Decode All Bases - Base Scheme Decoder',
    author='WHITEHELL097',
    url='https://github.com/WHITEHELL097/DECRYPTER',
    license='MIT',
    packages=[
        'src'
    ],
    py_modules=[
        'decrypter'
    ],
    install_requires=[
        'argparse',
        'colorama',
        'termcolor',
        'pathlib',
        'anybase32',
        'base36',
        'base58',
        'pybase62',
        'base91',
        'pybase100',
        'exifread',
        'opencv-python',
        'pytesseract'
    ],
    python_requires='>=3.0.0',
    entry_points={
        'console_scripts': [
            'decrypter = decrypter:main'
        ]
    }
)
