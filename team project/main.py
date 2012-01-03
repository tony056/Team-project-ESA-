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
from google.appengine.api import mail
from datetime import datetime
from datetime import timedelta

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



class basketproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = basketdata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))
class baseproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = basedata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))

class volleyballproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = volleyballdata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))

class tennisproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = tennisdata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))

class tabletennisproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = tabletennisdata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))

class soccerproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = soccerdata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))

class othersproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = othersdata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))

class badmintonproduct(webapp.RequestHandler):
    def get(self):
        productname = self.request.get('product')
        g = badmintondata.all()
        results = g.fetch(100)
            
        template_values={
            'g':g,
            'results':results,
            'productname':productname,
            }
        path = os.path.join(os.path.dirname(__file__),'productdata.txt')
        self.response.out.write(template.render(path, template_values))
class stupid(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""You are so stupid!! Please enter the bigger number!!<html><button onclick="location.href='/'"><b>Mainpage</b></button></html>""")
        
class buy(webapp.RequestHandler):
  def post(self):
    user=users.get_current_user()
    if user:
        productname=self.request.get('name')
        price=int(self.request.get('price'))
        p=basketdata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                if i.lowestprice < price:
                    i.lowestprice=price
                    i.buyer=users.get_current_user()
                    i.put()
                    self.redirect('/basketball')
                else:
                    self.redirect('/stupid')
        p=basedata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                i.lowestprice=price
                i.buyer=users.get_current_user()
                i.put()
                self.redirect('/baseball')
        p=volleyballdata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                i.lowestprice=price
                i.buyer=users.get_current_user()
                i.put()
                self.redirect('/volleyball')
        p=tabletennisdata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                i.lowestprice=price
                i.buyer=users.get_current_user()
                i.put()
                self.redirect('/tabletennis')
        p=tennisdata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                i.lowestprice=price
                i.buyer=users.get_current_user()
                i.put()
                self.redirect('/tennis')
        p=othersdata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                i.lowestprice=price
                i.buyer=users.get_current_user()
                i.put()
                self.redirect('/others')
        p=soccerdata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                i.lowestprice=price
                i.buyer=users.get_current_user()
                i.put()
                self.redirect('/soccer')
        p=badmintondata.all()
        re=p.fetch(100)
        for i in re:
            if i.name == productname:
                i.lowestprice=price
                i.buyer=users.get_current_user()
                i.put()
                self.redirect('/badminton')
    else:
        self.redirect('/login')
class maill(webapp.RequestHandler):
    def get(self):
        day = datetime.now()+timedelta(hours = 8)
        deadline = basketdata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
        deadline = basedata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
        deadline = badmintondata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
        deadline = volleyballdata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
        deadline = tennisdata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
        deadline = tabletennisdata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
        deadline = soccerdata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
        deadline = othersdata.all().filter("deadline <",day)
        for i in deadline:
            if i.buyer == i.author:
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Time is up, there is no one want to buy your product!"
                                        ,body="""Dear """+ i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction". I am sorry about that your product is still unmarketable.
                                                Maybe your can try to sell it again. Thank you for coming!! """)
                i.delete()
            else: 
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.author.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.buyer.email()+""" wants to buy your product.
                                                 You can discuss the details of the deal now. Thank you for coming!!""")
                message=mail.send_mail(sender="tony61507@gmail.com",to= i.buyer.email(),subject="Congratulations!!!"
                                        ,body="""Dear """+i.author.email()+""":
                                                    I am one of founders of the "E-Sports-Auction".Time is up! The user:"""+i.author.email()+""" can complete the transaction
                                                 with you. You can discuss the details of the deal now. Thank you for coming!!""")
                i.delete()
class helpp(webapp.RequestHandler):
    def get(self):
        template_values={
        
                }
        path = os.path.join(os.path.dirname(__file__), 'help.txt')
        self.response.out.write(template.render(path, template_values))
class Image (webapp.RequestHandler):
  def get(self):
    Imge = db.get(self.request.get("img"))
    if Imge.image:
      self.response.headers['Content-Type'] = "image/jpg"
      self.response.out.write(Imge.image)
    else:
      self.response.out.write("No image")
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
    num = db.IntegerProperty()
    num=0
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class basedata(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class badmintondata(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class tennisdata(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class tabletennisdata(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class soccerdata(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class volleyballdata(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class othersdata(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    lowestprice = db.IntegerProperty()
    method = db.StringProperty()
    new = db.StringProperty()
    size = db.FloatProperty()
    text = db.TextProperty()
    buyer = db.UserProperty()
    nowtime = db.DateTimeProperty(auto_now_add = True)
    deadline = db.DateTimeProperty()
    deadline2 = db.StringProperty()
    image = db.BlobProperty()
class selldata(webapp.RequestHandler):
    def post(self):
        if self.request.get('judge') == "on":
            Database=basketdata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image = self.request.get('img')
            Database.image = db.Blob(image)
            Database.num=Database.num+1
            Database.put()
            self.redirect('/basketball')
        elif self.request.get('judge2') == "on":
            Database=basedata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/baseball')
        elif self.request.get('judge7') == "on":
            Database=badmintondata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/badminton')
        elif self.request.get('judge4') == "on":
            Database=soccerdata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/soccer')
        elif self.request.get('judge3') == "on":
            Database=volleyballdata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/volleyball')
        elif self.request.get('judge5') == "on":
            Database=tennisdata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/tennis')
        elif self.request.get('judge6') == "on":
            Database=tabletennisdata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/tabletennis')
        elif self.request.get('judge8') == "on":
            Database=othersdata()
            Database.author=users.get_current_user()
            Database.buyer=users.get_current_user()
            Database.name=self.request.get('name')
            Database.lowestprice=int(self.request.get('lowestprice'))
            Database.new=self.request.get('new')
            Database.method=self.request.get('method')
            Database.size=float(self.request.get('size'))
            Database.text=self.request.get('text')
            Database.deadline=datetime.strptime(self.request.get('deadline'),"%b %d, %Y %H:%M:%S")
            Database.deadline2=self.request.get('deadline')
            image=self.request.get('img')
            Database.image = db.Blob(image)
            Database.put()
            self.redirect('/others')
        
#class search(webapp.RequestHandler):
class basketball(webapp.RequestHandler):
    def get(self):
        q = basketdata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'basketball.txt')        
        self.response.out.write(template.render(path, template_values))

class volleyball(webapp.RequestHandler):
    def get(self):
        q = volleyballdata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'volleyball.txt')        
        self.response.out.write(template.render(path, template_values))


class soccer(webapp.RequestHandler):
    def get(self):
        q = soccerdata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'soccer.txt')        
        self.response.out.write(template.render(path, template_values))

class tennis(webapp.RequestHandler):
    def get(self):
        q = tennisdata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'tennis.txt')        
        self.response.out.write(template.render(path, template_values))
class tabletennis(webapp.RequestHandler):
    def get(self):
        q = tabletennisdata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'tabletennis.txt')        
        self.response.out.write(template.render(path, template_values))

class badminton(webapp.RequestHandler):
    def get(self):
        q = badmintondata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'badminton.txt')        
        self.response.out.write(template.render(path, template_values))
class others(webapp.RequestHandler):
    def get(self):
        q = othersdata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'others.txt')        
        self.response.out.write(template.render(path, template_values))
class baseball(webapp.RequestHandler):
    def get(self):
        q = basedata.all()
        q.order('-name')
        results = q.fetch(20)
        template_values = {
            "a":[1,2,5,7],
            'q':q,
            'results':results
            }
        
        path = os.path.join(os.path.dirname(__file__), 'baseball.txt')        
        self.response.out.write(template.render(path, template_values))
def main():
    application = webapp.WSGIApplication([('/', Mainpage),('/login',login),('/logout',logout),('/basketball',basketball),('/sell',sell),('/selldata',selldata),('/volleyball',volleyball),('/soccer',soccer)
                                          ,('/tennis',tennis),('/tabletennis',tabletennis),('/badminton',badminton)
                                          ,('/others',others),('/image',Image),('/mail/weekly',maill),('/buy',buy),('/baseball',baseball),('/stupid',stupid),
                                          ('/help',helpp)
                                          ,('/basketproduct',basketproduct),('/baseproduct',baseproduct),('/volleyballproduct',volleyballproduct),
                                          ('/tennisproduct',tennisproduct),
                                          ('/tabletennisproduct',tabletennisproduct),('/soccerproduct',soccerproduct)
                                          ,('/badmintonproduct', badmintonproduct),('/othersproduct',othersproduct)],debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
