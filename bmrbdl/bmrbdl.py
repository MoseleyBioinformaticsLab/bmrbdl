#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bmrbdl.bmrbdl
~~~~~~~~~~~~~
Routines for downloading NMR-STAR formatted files from the BMRB
website to local computer.
"""

from __future__ import print_function, division

import requests
import lxml.html
import os


def collect_ids(base_url):
    """Collects entries id from the BMRB web site.
    
    :param str base_url: URL address from which files will be downloaded. 
    :return: List of ids.
    :rtype: :py:class:`list`
    """

    # Create a handle (page) to handle the contents of the website
    page = requests.get(base_url)

    # Store the contents of the website under doc
    doc = lxml.html.fromstring(page.content)

    # Parse data that are stored between <tr>..</tr> of the site's HTML code
    tr_elements = doc.xpath("//tr")

    nmrstar_ids_list = []
    for i in tr_elements:
        lst = list(i.text_content().split("."))
        try:
            bmrb_id = "".join(i for i in lst[0] if i.isdigit())
            bmrb_id_int = int(bmrb_id)  # try to convert to int.
        except ValueError:
            continue  # continue if id cannot be converted into integer

        nmrstar_ids_list.append(bmrb_id)  # add file id into list of ids
    
    return nmrstar_ids_list


def bmrbdl(ids_list, 
           base_url="http://www.bmrb.wisc.edu/ftp/pub/bmrb/entry_lists/nmr-star3.1/", 
           output_dir="NMR-STAR3",
           prefix="bmr", 
           extension="str",
           verbose=False):
    """Download entries in NMR-STAR format from BMRB.
    
    :param list or tuple ids_list: List of BMRB file ids. 
    :param str base_url: URL address from which files will be downloaded.
    :param str output_dir: Path to directory where files will be downloaded. 
    :param str prefix: File prefix. 
    :param str extension: File extension.
    :param verbose: Print more information.
    :type verbose: :py:obj:`True` or :py:obj:`False`
    :return: :py:obj:`None`
    """
    for bmrb_id in ids_list:
        file_url = base_url + "/" + prefix + bmrb_id + "." + extension
        file_name = output_dir + "/" + prefix + bmrb_id + "." + extension

        if os.path.exists(file_name):
            if verbose:
                print("Skipping:", bmrb_id, "already exists.")
            continue
        
        if verbose:
            print("Processing:", bmrb_id)

        r = requests.get(file_url)

        if r.status_code == requests.codes.ok:
            data = r.text

            # create directory if it does not exist
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)

            with open(file_name, 'w') as outfile:
                outfile.write(data)
        else:
            if verbose:
                print("Error code:", r.status_code, "for BMRBID:", bmrb_id)
