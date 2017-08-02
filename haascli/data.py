import click


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.pass_context
def cli(ctx, **kwargs):
    """Data related operations
    """
    ctx.obj.update(kwargs)


@cli.command()
@click.pass_context
def save(ctx):
    pass


@cli.command()
@click.pass_context
def restore(ctx):
    pass


@cli.command()
@click.pass_context
def resize(ctx):
    pass
