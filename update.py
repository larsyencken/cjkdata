#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  update.py
#  cjktools-data
#

import sys
import optparse
import codecs
import urllib2
import gzip
from cStringIO import StringIO

from consoleLog import default as _log

DICTIONARIES = {
    'cjkdata/dict/je_edict': 'http://ftp.monash.edu.au/pub/nihongo/edict.gz',
    'cjkdata/dict/je_enamdict': 'http://ftp.monash.edu.au/pub/nihongo/enamdict.gz',  # nopep8
    'cjkdata/dict/je_compdic': 'http://ftp.monash.edu.au/pub/nihongo/compdic.gz',  # nopep8
    'cjkdata/kanjidic': 'http://ftp.monash.edu.au/pub/nihongo/kanjidic.gz',
    'cjkdata/kanjd212': 'http://ftp.monash.edu.au/pub/nihongo/kanjd212.gz',
    'cjkdata/radkfile': 'http://ftp.monash.edu.au/pub/nihongo/radkfile.gz',
}


def update():
    _log.start('Updating %d dictionaries' % len(DICTIONARIES),
               nSteps=len(DICTIONARIES))

    for target_name, url in sorted(DICTIONARIES.items()):
        _log.log(target_name)
        gzdata = urllib2.urlopen(url).read()
        istream = gzip.GzipFile(fileobj=StringIO(gzdata), mode='r')
        uistream = codecs.getreader('euc-jp')(istream)

        with codecs.open(target_name, 'w', 'utf8') as ostream:
            for line in uistream:
                ostream.write(line)

        uistream.close()
        istream.close()

    _log.finish()


def _create_option_parser():
    usage = \
"""%prog [options]

Checks for updated versions of each dictionary."""  # nopep8

    parser = optparse.OptionParser(usage)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    update()

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    main(sys.argv[1:])

# vim: ts=4 sw=4 sts=4 et tw=78:
