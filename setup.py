from setuptools import setup, find_packages

setup(
    name='pattern-outlier',
    version='0.1.0',
    description='A Python library for detecting outliers based on frequent pattern mining.',
    author='Alexander Li',
    author_email='lihangalex@pm.me',
    url='https://github.com/lihangalex/pattern-outlier',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'mlxtend',
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
