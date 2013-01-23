#!/usr/bin/env python
#
import os
import webapp2
import base_handlers
from public import content

app = webapp2.WSGIApplication([
			# Public Handlers
			('/?$',	content.Home),							
			('/.*', base_handlers.NotFoundHandler)
			],
		  debug=True)
