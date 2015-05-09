#!/usr/bin/env python
import os
import jinja2
import webapp2
from datetime import datetime


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        stevilo = 31
        ura = datetime.now().strftime("%Y-%M-%D" "%H-%M-%S")
        seznam = ["bla", "ha", "jupi"]
        params = {"stevilo":stevilo, "lista": seznam, "ura":ura}
        self.render_template("hello.html", params)

class DrugaUra(BaseHandler):
    def get(self):
        ura = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        params = {"ura":ura}
        self.render_template("ura.html", params)


class KrNekiHandler(BaseHandler):
    def get(self):
        self.write("hello, world!")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/hello', KrNekiHandler),
    webapp2.Route('/ura', DrugaUra)
], debug=True)
# Trenutni_cas
