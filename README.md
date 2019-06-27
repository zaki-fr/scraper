# scraper

The scraper has a pupose to scrape the data from Volume 2 of the Guide of Ministry of Solidarity and Health.
The data are:
 - List of acts
 - List of diagnostics
 - List of GHMs
The scraper is designed in Java8 and Python 3.7.

## Requirements:

### The libraries required for Python:
- Pandas
- Sys
- Re
- codecs
- os
- subprocess
- argparse
- pathlib

### The Jar files required for Java.
- PDFBox 2.0.3
- Commons-Logging 1.2
- fontbox 2.0.15

How it Works

In windows open your cmd and go the directory of where your scraper package is and there the instructions

usage: scraper.py [-h] [--file FILE] [--diag DIAG] [--act ACT] [--ghm GHM]

Scraping options of Medical Volume2

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Volume2 path that you need to extract
  --diag DIAG  option to extract lists of diagnostics
  --act ACT    option to extract lists of acts
  --ghm GHM    option to extract lists of GHMs

after file argument you should put the file of volume2
if you want to extract the list of acts you should put --act y
