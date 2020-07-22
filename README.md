# Overview

SQL + Jinja Done Right™

This project is a thin wrapper around [Jinja](https://jinja.palletsprojects.com/) templates to help
manage the generation of SQL.

In your project create a directory name `sql/templates` to manage your SQL files:

```sh
.
└── sql
    └── templates
        ├── foo.sql
        └── bar.sql
```

Templates are also search from the current working directory and will have priority over
files in `sql/templates`.

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

In `bar.sql` lets try including `foo.sql`:

```sql
SELECT * FROM ({% include 'foo.sql' %}) as t1
```

The rendered SQL would be:
```sql
SELECT * FROM (SELECT 'Hello World' as message) as t1
```

## Command Line Interface

The Python interface makes sense at runtime, but for development the CLI is more convenient.

The library installs a CLI script: `sql`

```sh
$ sql --help
Usage: sql [OPTIONS] SRC

Options:
--template_path TEXT  Base directory where SQL templates are located.
Defaults to `sql/templates`

--help                Show this message and exit.
```

To see the resulting SQL we can try:

```sh
sql foo.sql msg='Hello World'

# => SELECT 'Hello World' as message
```

## Installation

```sh
pip install sql-ninja
```

Or add to `requirements.txt`

```txt
sql-ninja
```

Or add to `setup.py`

```python
setup(
    install_requires=[
        'sql-ninja',
    ]
```

## Docker

Docker users can pull directly from `ddrscott/sql-ninja`

```sh
docker run --rm -v $PWD:/app -w /app ddrscott/sql-ninja sample.sql
#            ^   ^            ^      ^                  ^
#            |   |            |      |                  |
#            |   |            |      |                  + the template
#            |   |            |      |
#            |   |            |      + the image
#            |   |            |
#            |   |            + start in /app path
#            |   |            
#            |   + volume mount current path to /app
#            |
#            + remove container when complete
```

## Contributing

Bug reports and pull requests are welcome on GitHub at
https://github.com/ddrscott/sql-ninja


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
