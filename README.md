python-autocite
============

python-autocite provides modules and a command line utility
for automatically generating citiations of web pages.

Licensed under the MIT license. Though not required by the
license, please consider dropping a line if you find this
software useful.


Diff from the [original repo](https://github.com/thenaterhood/python-autocite)
-----------
Updated for [UWE-Harvard referencing](https://www.uwe.ac.uk/study/study-support/study-skills/referencing/uwe-bristol-harvard#webpages) (webpage format), not perfect, stil working on it. Italics only work with supported terminals in CLI mode. Cites in uwe mode by default (original repo formats into apa).

Installation
------------

Requirements:

* BeautifulSoup4
* Requests
* Dateutil
* Python 3
* (optional) pageres - for capturing screenshots

Run `python setup.py install` to install.

Usage
-----------
Command line usage:

Run `autocite --help` to see the help text.

Protip: Missing information will be filled in with "[[[field name]]]" which should make it easy to search for.

Currently only supports APA, but is extensible for other formats.

Using in other programs:

`from python_autocite.lib import *`

The modules available are:
* `python_autocite.lib.datafinder.Datafinder` - attempts to pull
publication information from a BeautifulSoup soup
* `python_autocite.lib.citation.Citation` - Contains citation data, 
with intelligent setters
* `python_autocite.lib.formatter.CitationFormatter` - Interface for
creating citation formatters
* `python_autocite.lib.formatter.APAFormatter` - formats a Citation
into an APA citation

Examples
-----------

Cite a single URL:

`autocite --url http://arstechnica.com/business/2012/12/report-data-caps-just-a-cash-cow-for-internet-providers/`

This will print to stdout:

`Anderson, N. (2012, December 18). Report: data caps just a “cash cow” for Internet providers. Retrieved June 18, 2017, from http://arstechnica.com/business/2012/12/report-data-caps-just-a-cash-cow-for-internet-providers/`

Cite a list of URLs (newline separated), and save the citations to a file called citations.txt

`autocite --from-file urllist.txt --to-text citations.txt`

Optionally, you can add the `--capture` flag to capture screenshots of websites. This will not work for all
websites, and may increase the time to generate citations significantly. Each capture will be stored in the current
directory.

Disclaimers
-----------
This software is not perfect and will make mistakes. Check that
your citations are correct before using them for any important
purpose.

