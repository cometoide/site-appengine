#!/usr/bin/env python
#
import os
import webapp2
import base_handlers

class Home(base_handlers.BasicHandler):

	def get(self):
		file_name = 'public/index.html'
		template_values = {}
		self.render_response(file_name,**template_values)
