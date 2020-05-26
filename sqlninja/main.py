import click
import os
from sqlninja import engine

@click.command(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.argument('src')
@click.option('--template_path', default='sql/templates', help='Base directory where SQL templates are located. Defaults to `sql/templates`')
@click.pass_context
def cli(ctx, src, template_path):

    # All remaining arguments are passed through to render context
    context = dict([arg.split('=') for arg in ctx.args if '=' in arg ])

    click.echo(
        engine.render(
            name=src,
            jinja_env=engine.default_jinja_env(template_path),
            **context
        )
    )
