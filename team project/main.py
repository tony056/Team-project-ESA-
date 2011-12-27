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
          
          #self.response.headers['Content-Type'] = 'text/plain'
          self.response.out.write('Hello, ' + user.nickname())
          self.response.out.write("""<div><button onclick="location.href='/'">MainPage</button></div></body></html>""")
        else:
          self.redirect(users.create_login_url(self.request.uri))
class logout(webapp.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))
#class database(db.Model):
    #name = db.StringProperty()
    #lowestprice = db.IntegerProperty()
    #method = db.StringProperty()
    #new = db.StringProperty()
    #size = db.FloatProperty()
    #text = db.TextProperty()
class sell(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template_values={
        
                }
            path = os.path.join(os.path.dirname(__file__), 'sell.txt') 
            self.response.out.write(template.render(path, template_values))
        else:
          self.redirect(users.create_login_url(self.request.uri))  
class basketdata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class basedata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class badmintondata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class tennisdata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class tabletennisdata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class soccerdata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class volleyballdata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class othersdata(db.Model):
    author = users.get_current_user()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = users.get_current_user()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.StringProperty()
    image = db.BlobProperty()
class selldata(webapp.RequestHandler):
    def post(self):
        if self.request.get('judge') == "on":
            self.response.out.write('yes')
            Database=basketdata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/basketball')
        elif self.request.get('judge2') == "on":
            Database=basedata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/baseball')
        elif self.request.get('judge7') == "on":
            Database=badmintondata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/badminton')
        elif self.request.get('judge4') == "on":
            Database=soccerdata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/soccer')
        elif self.request.get('judge3') == "on":
            Database=volleyballdata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/volleyball')
        elif self.request.get('judge5') == "on":
            Database=tennisdata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/tennis')
        elif self.request.get('judge6') == "on":
            Database=tabletennisdata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/tabletennis')
        elif self.request.get('judge8') == "on":
            Database=othersdata()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/others')
        
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
    application = webapp.WSGIApplication([('/', Mainpage),('/login',login),('/logout',logout),('/basketball',basketball),('/sell',sell),('/selldata',selldata),('/volleyball',volleyball),('/soccer',soccer)
                                          ,('/tennis',tennis),('/tabletennis',tabletennis),('/badminton',badminton),('/others',others),('/baseball',baseball)],debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
