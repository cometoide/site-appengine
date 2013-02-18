#!/usr/bin/env python
#
# Copyright 2012 Cometoide.
# @author: samiq
#
import os
import logging
import webapp2
from webapp2_extras import jinja2

logging.getLogger().setLevel(logging.DEBUG)

class BasicHandler(webapp2.RequestHandler):
	def get(self):
		# Default handler for get requests
		self.response.error(400)
	
	def post(self):
		# Default handler for post requests
		self.response.error(400)

	def not_found(self):
		# Sends an 404 error back to the browser.
		self.response.set_status(404)
		self.render_response("404.html")
				
	@webapp2.cached_property
	def jinja2(self):
		# Returns a Jinja2 renderer cached in the app registry.
		return jinja2.get_jinja2(app=self.app)

	def render_response(self, _template, **context):
		# Renders a template and writes the result to the response.		
		rv = self.jinja2.render_template(_template, **context)
		self.response.write(rv)

class NotFoundHandler(BasicHandler):
	def get(self):
		self.response.error(400)