#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bmrbdl command-line interface

Usage:
    bmrbdl -h | --help
    bmrbdl --version
    bmrbdl [<id>...] [--url=<address>] [--prefix=<value>] [--extension=<value>] [--output-dir=<dir-name>] [--verbose]

Options:
    -h, --help                      Show this screen.
    --version                       Show version.
    --verbose                       Print what files are processing.
    --output-dir=<dir-name>         Where to download files [default: NMRSTAR].
    --url=<address>                 Base URL to download from [default: http://www.bmrb.wisc.edu/ftp/pub/bmrb/entry_lists/nmr-star3.1/] 
    --prefix=<value>                File prefix [default: bmr].
    --extension=<value>             File extensions [default: .str].
"""

from . import bmrbdl


def cli(cmdargs):
    """Process command-line arguments and execute downloader.
    :param dict cmdargs: Dictionary of command-line arguments.
    """
    bmrb_ids = cmdargs["<id>"]
    base_url = cmdargs["--url"]

    if not bmrb_ids:
        bmrb_ids = bmrbdl.collect_ids(base_url=base_url)

    bmrbdl.bmrbdl(ids_list=bmrb_ids,
                  base_url=base_url,
                  output_dir=cmdargs["--output-dir"],
                  prefix=cmdargs["--prefix"],
                  extension=cmdargs["--extension"],
                  verbose=cmdargs["--verbose"])
