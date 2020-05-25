import os
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape
from sqlninja.utils import once

DEFAULT_TEMPLATE_PATH = 'sql/templates'

default_jinja_context = {}
"""
Override to provide default context to Jinja's render function.

Defaults to empty dictionary.
"""


def default_jinja_env(template_path: str = None):
    if template_path is None:
        template_path = DEFAULT_TEMPLATE_PATH

    return Environment(
        loader=FileSystemLoader(template_path),
        autoescape=select_autoescape(['sql'])
    )


def render(name: str, jinja_env: Environment=None, **context):
    """
    Renders template with `name`.

    :param name: name of the template. Can also contain
    :param context: context provided to Jinja template. Defaults to `default_jinja_context`
    :param jinja_env: Full Jinja environment containing all templates. Defaults to `default_jinja_context`
    """
    run_config()

    if jinja_env is None:
        jinja_env = default_jinja_env()

    if context is None:
        context = default_jinja_context

    for path in jinja_env.loader.searchpath:
        name = name.replace(path, '')

    template = jinja_env.get_template(name)
    return template.render(**context)


@once
def run_config(config_file: str = ".sqlninja") -> None:
    """
    Execute config script when it exists

    Credits: https://github.com/prompt-toolkit/ptpython/blob/89017ba158ed1d95319233fa5aedf3931c3b8b77/ptpython/repl.py#L274

    :param config_file: Path of the configuration file.
    """

    # Expand tildes.
    config_file = os.path.expanduser(config_file)

    # Check whether this file exists.
    if not os.path.isfile(config_file):
        return

    namespace: Dict[str, Any] = {}

    with open(config_file, "rb") as f:
        code = compile(f.read(), config_file, "exec")
        exec(code, namespace, namespace)

    if 'configure' in namespace:
        namespace["configure"](sys.modules[__name__])
