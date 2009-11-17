import config
#!/usr/bin/env python
#
# Copyright (c) 2009 Michael D. Hall
# Licensed under the MIT License.
#

__author__ = "Michael D. Hall"
__date__ = "$Nov 17, 2009 6:31:57 AM$"

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers import site


ROUTES = [('/*$', site.DefaultHandler), ]

def main():
  application = webapp.WSGIApplication(ROUTES, debug=config.DEBUG)
  run_wsgi_app(application)

if __name__ == "__main__":
  print "Hello World"
