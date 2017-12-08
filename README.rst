bmrbdl
======

The ``bmrbdl`` package provides a simple Python interface for downloading
NMR-STAR formatted files from BMRB_ repository.

Installation
~~~~~~~~~~~~

Install on Linux, Mac OS X
--------------------------

.. code:: bash

   python3 -m pip install git+git://github.com/MoseleyBioinformaticsLab/bmrbdl.git


Install on Windows
------------------

.. code:: bash

   py -3 -m pip install git+git://github.com/MoseleyBioinformaticsLab/bmrbdl.git


Usage example
~~~~~~~~~~~~~

Command-line interface
----------------------

.. code-block:: none

   Usage:
       bmrbdl -h | --help
       bmrbdl --version
       bmrbdl [<id>...] [--url=<address>] [--prefix=<value>] [--extension=<value>]
              [--output-dir=<dir-name>] [--verbose]

   Options:
       -h, --help                      Show this screen.
       --version                       Show version.
       --verbose                       Print what files are processing.
       --output-dir=<dir-name>         Where to download files [default: NMRSTAR].
       --url=<address>                 Base URL to download from
                                       [default: http://www.bmrb.wisc.edu/ftp/pub/bmrb/entry_lists/nmr-star3.1/]
       --prefix=<value>                File prefix [default: bmr].
       --extension=<value>             File extensions [default: str].


* To download several NMR-STAR formatted files (NMR-STAR version 3):

.. code-block:: none

   python3 -m bmrbdl 15000 18569 --url=http://www.bmrb.wisc.edu/ftp/pub/bmrb/entry_lists/nmr-star3.1/ \
                                 --output-dir=NMRSTAR3 --prefix=bmr --verbose

* To download several NMR-STAR formatted files (NMR-STAR version 2):

.. code-block:: none

   python3 -m bmrbdl 15000 18569 --url=http://www.bmrb.wisc.edu/ftp/pub/bmrb/entry_lists/nmr-star2.1/ \
                                 --output-dir=NMRSTAR2 --prefix=bmr --verbose

* In order to download all files just omit BMRB ids:

.. code-block:: none

   python3 -m bmrbdl --url=http://www.bmrb.wisc.edu/ftp/pub/bmrb/entry_lists/nmr-star3.1/ \
                     --output-dir=NMRSTAR3 --prefix=bmr --verbose

* To download metabolomics data (experimental entries):

.. code-block:: none

   python3 -m bmrbdl --url=http://www.bmrb.wisc.edu/ftp/pub/bmrb/metabolomics/NMR_STAR_experimental_entries/ \
                     --output-dir=NMRSTARBMSE --prefix=bmse --verbose

* To download metabolomics data (theoretical entries):

.. code-block:: none

   python3 -m bmrbdl --url=http://www.bmrb.wisc.edu/ftp/pub/bmrb/metabolomics/NMR_STAR_theoretical_entries/ \
                     --output-dir=NMRSTARBMST --prefix=bmst --verbose


.. _BMRB: http://www.bmrb.wisc.edu