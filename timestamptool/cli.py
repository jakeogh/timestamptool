#!/usr/bin/env python3

import click
from asserttool import ic
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tvicgvd
from globalverbose import gvd
from mptool import output

from timestamptool import get_timestamp


@click.command()
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx: click.Context,
    verbose_inf: bool,
    dict_output: bool,
    verbose: bool = False,
) -> None:
    tty, verbose = tvicgvd(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
        ic=ic,
        gvd=gvd,
    )

    output(
        get_timestamp(),
        reason=None,
        dict_output=dict_output,
        tty=tty,
    )
