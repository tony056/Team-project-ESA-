#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from google.appengine.ext.webapp import template
import cgi
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class Mainpage(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }

        path = os.path.join(os.path.dirname(__file__), 'mainpage.txt')
        self.response.out.write(template.render(path, template_values))
class login(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
          
          self.response.headers['Content-Type'] = 'text/plain'
          self.response.out.write('Hello, ' + user.nickname())
        else:
          self.redirect(users.create_login_url(self.request.uri))
#class search(webapp.RequestHandler):
class basketball(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'basketball.txt')        
        self.response.out.write(template.render(path, template_values))

class volleyball(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'volleyball.txt')        
        self.response.out.write(template.render(path, template_values))


class soccer(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'soccer.txt')        
        self.response.out.write(template.render(path, template_values))

class tennis(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'tennis.txt')        
        self.response.out.write(template.render(path, template_values))
class tabletennis(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'tabletennis.txt')        
        self.response.out.write(template.render(path, template_values))

class badminton(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'badminton.txt')        
        self.response.out.write(template.render(path, template_values))
class others(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'others.txt')        
        self.response.out.write(template.render(path, template_values))
class baseball(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        
        path = os.path.join(os.path.dirname(__file__), 'baseball.txt')        
        self.response.out.write(template.render(path, template_values))
def main():
    application = webapp.WSGIApplication([('/', Mainpage),('/login',login),('/basketball',basketball),('/volleyball',volleyball),('/soccer',soccer)
                                          ,('/tennis',tennis),('/tabletennis',tabletennis),('/badminton',badminton),('/others',others),('/baseball',baseball)],debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
