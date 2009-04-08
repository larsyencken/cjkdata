# -*- coding: utf-8 -*-
#
#  __init__.py
#  cjktools_data
# 
#  Created by Lars Yencken on 08-04-2009.
#  Copyright 2009 Lars Yencken. All rights reserved.
#

import pkg_resources
import codecs

def open_file(filename):
    return codecs.getreader('utf8')(
            pkg_resources.resource_stream(__name__, filename)
        )

def read_file(filename):
    return pkg_resources.resource_string(__name__, filename).decode('utf8')

# vim: ts=4 sw=4 sts=4 et tw=78:
