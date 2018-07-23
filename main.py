import jinja2
import os
import webapp2
import model

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('templates/main.html')
        html = main_template.render()
        self.response.write(html)

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        sign_up_template = jinja_env.get_template('templates/signup.html')
        html = sign_up_template.render()
        self.response.write(html)

class PersonHandler(webapp2.RequestHandler):
    def post(self):
        person = model.Person()
        person.name = self.request.get("name")
        person.college = self.request.get("college")
        person.put()
        self.response.write("Saved!")

app = webapp2.WSGIApplication([
    ('/', MainHandler), # asking for slash, construct main handlers
    ('/signup', SignUpHandler),
    ('/profile', PersonHandler)
], debug = True)
