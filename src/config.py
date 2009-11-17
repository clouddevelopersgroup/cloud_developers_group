import os.path
#!/usr/bin/env python
#
# Copyright (c) 2009 Michael D. Hall
# Licensed under the MIT License.
#

__author__="just3ws"
__date__ ="$Nov 17, 2009 8:21:58 AM$"

import os
import logging

APP_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')
