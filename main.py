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

class MapHandler(webapp2.RequestHandler):
    def get(self):
        Arc_Main_template = jinja_env.get_template('templates/ArcMain.html')
        # query = model.Person.query().filter(model.Person.username == self.request.get("username"))
        # student = query.get()
        html = Arc_Main_template.render(
            # "lat1": student.lat1,
            # "long1": student.long1,
            # "lat2": student.lat2,
            # "long2": student.long2
        )
        self.response.write(html)

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        sign_up_template = jinja_env.get_template('templates/signup.html')
        html = sign_up_template.render()
        self.response.write(html)

class PersonHandler(webapp2.RequestHandler):
    def post(self):
        person = model.Person()
        person.username = self.request.get("username")
        person.name = self.request.get("name")
        person.college = self.request.get("college")
        person.long1 = float(self.request.get("long1"))
        person.lat1 = float(self.request.get("lat1"))
        person.highschool = self.request.get("highschool")
        person.long2 = float(self.request.get("long2"))
        person.lat2 = float(self.request.get("lat2"))
        key=person.put()
        self.response.write("Profile created!")
        print(key.get())
class PersonFile(webapp2.RequestHandler):
    def get(self):
        person_query = model.Person.query()
        all_people = person_query.fetch()
        list_template = jinja_env.get_template('templates/profile.html')
        html = list_template.render({
            "people": all_people
        })
        self.response.write(html)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_template = jinja_env.get_template('templates/login.html')
        html = login_template.render()
        self.response.write(html)

class Retrieve(webapp2.RequestHandler):
    def get(self):
        query = model.Person.query().filter(model.Person.username == self.request.get("username"))
        student = query.get()
        user_template = jinja_env.get_template('templates/userprofile.html')
        html = user_template.render({
            "name": student.name,
            "highschool": student.highschool,
            "college": student.college
        })
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignUpHandler),
    ('/profile', PersonHandler),
    ('/profile/user', PersonFile),
    ('/login', LoginHandler),
    ('/userprofile', Retrieve),
    ('/map', MapHandler)
], debug = True)
