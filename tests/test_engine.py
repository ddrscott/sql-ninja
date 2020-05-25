from sqlninja import engine

def jinja_env():
    return engine.default_jinja_env('tests/sql/templates')


def test_color():
    expected = (
        "SELECT\n"
        "    'red' as color"
    )
    result = engine.render(
        name='color.sql',
        jinja_env=jinja_env()
    )
    assert result == expected


def test_strip_default_path():
    expected = 'SELECT 1'
    result = engine.render(
        name='./tests/sql/templates/select_1.sql',
        jinja_env=jinja_env()
    )
    assert result == expected

def test_color_from_context():
    expected = "blue"
    engine.run_config('tests/sqlninja_context.py')
    result = engine.render(
        name='color_from_context.sql',
        jinja_env=jinja_env(),
        color='blue'
    )
    assert result == expected

def test_complex():
    expected = (
        "SELECT\n"
        "  *\n"
        "FROM (SELECT 'bar' as child) AS t1"
    )
    result = engine.render(
        name='complex/parent.sql',
        jinja_env=jinja_env()
    )
    assert result == expected
