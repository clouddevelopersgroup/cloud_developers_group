import os.path

import config
#!/usr/bin/env python
#
# Copyright (c) 2009 Michael D. Hall
# Licensed under the MIT License.
#

__author__ = "Michael D. Hall"
__date__ = "$Nov 17, 2009 7:18:56 AM$"




from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

_DEBUG = True

class DefaultHandler(webapp.RequestHandler):
  def get(self):
    path = os.path.join(config.APP_ROOT_DIR, os.path.join('views', 'base.html'))
    self.response.out.write(template.render(path, {}, debug=_DEBUG))