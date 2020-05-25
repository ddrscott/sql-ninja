# Overview

SQL + Jinja Done Right™

This project is a thing wrapper around [Jinja](https://jinja.palletsprojects.com/) templates to help
manage the generation of SQL.

In your project create a directory name `sql/templates` to manage you SQL files:

```sh
.
└── sql
    └── templates
        ├── foo.sql
        └── bar.sql
```

An example `foo.sql` might be:

```sql
SELECT '{{msg}}' as message
```

Then to access the SQL template use the following Python snippet:

```python
from sqlninja import engine as sqlninja

query = sqlninja.render("foo.sql", msg="Hello World")
```

The resulting `query` would be:
```sql
SELECT 'Hello World' as message
```

## Command Line Interface

The Python interface makes sense at runtime, but for development the CLI is more convenient.

So see the resulting SQL we can try:

```sh
sql foo.sql msg='Hello World'

# => SELECT 'Hello World' as message
```

## Installation

```sh
pip install sql-ninja
```

or add to `requirements.txt`

```txt
sql-ninja
```

or add to `setup.py`

```python
setup(
    install_requires=[
        'sql-ninja',
    ]
```


## Contributing

Bug reports and pull requests are welcome on GitHub at
https://github.com/ddrscott/sql-ninja


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
