from setuptools import setup

setup(
    name='sql-ninja',
    version='0.1',
    author='Scott Pierce',
    author_email='ddrscott@gmail.com',
    description='SQL + Jinja Templates Done Right™',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
    url='https://github.com/ddrscott/sql-ninja',
    packages=['sqlninja'],
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
