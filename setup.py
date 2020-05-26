from setuptools import setup

setup(
    name='sql-ninja',
    version='0.1.2',
    author='Scott Pierce',
    author_email='ddrscott@gmail.com',
    description='SQL + Jinja Templates Done Right™',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ddrscott/sql-ninja',
    packages=['sqlninja'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'click',
        'jinja2',
    ],
    entry_points={
        'console_scripts':[
            "sql = sqlninja.main:cli",
        ],
    }
)
