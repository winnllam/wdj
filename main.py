import jinja2
import os
import webapp2
import model
from webapp2_extras import json

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
        html = Arc_Main_template.render({

        })
        self.response.write(html)

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        sign_up_template = jinja_env.get_template('templates/signup.html')
        html = sign_up_template.render()
        self.response.write(html)
#USERINPUT USERINPUT USERINPUT
class PersonHandler(webapp2.RequestHandler):
    def post(self):
        person = model.Person()
        person.email = self.request.get("email")
        person.name = self.request.get("name")
        person.highschool = self.request.get("highschool")
        person.city1 = self.request.get("city1")
        person.state1 = self.request.get("state1")
        person.hslat = 0.0
        person.hslong = 0.0
        person.college = self.request.get("college")
        person.city2 = self.request.get("city2")
        person.state2 = self.request.get("state2")
        person.collat = 0.0
        person.collong = 0.0

        person.put()
    #    key=person.put()
        self.response.write("Profile created!")
    #    print(key.get())
#DISPLAYSEVERYON DISPLAYSEVERYONE DISPLAYEVERYONE
class PersonFile(webapp2.RequestHandler):
    def get(self):
        person_query = model.Person.query()
        all_people = person_query.fetch()
        list_template = jinja_env.get_template('templates/list.html')
        html = list_template.render({
            "people": all_people
        })
        self.response.write(html)
# JSON JSON JSON JSON JSON JSON
class Personlatlong(webapp2.RequestHandler):
    def get(self):
        person_query = model.Person.query()
        all_people = person_query.fetch()
        self.response.headers['Content-Type'] = 'application/json'
        def persontodict(all_people):
            latlong=[]
            for person in all_people:
                latlong.append({
                "lat1":person.lat1,
                "long1":person.long1,
                "lat2":person.lat2,
                "long2":person.long2
                })
            return latlong
        person_dictionaries= persontodict(all_people)
        self.response.write(json.encode(person_dictionaries))
#LOGIN LOGIN LOGIN
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_template = jinja_env.get_template('templates/login.html')
        html = login_template.render()
        self.response.write(html)
#DISPLAY PROFILE BASED ON EMAIL
class RetrieveProfile(webapp2.RequestHandler):
    def get(self):
        query = model.Person.query().filter(model.Person.email == self.request.get("email"))
        student = query.get()
        user_template = jinja_env.get_template('templates/profile.html')

        html = user_template.render({
            "name": student.name,
            "highschool": student.highschool,
            "college": student.college,
            "city1": student.city1,
            "state1": student.state1
        })
        self.response.write(html)
# DISPLAY EVERYONE IN THE SAME HIGHSCHOOL
class RetrieveHighschool(webapp2.RequestHandler):
    def get(self):
        query = model.Person.query().filter(model.Person.highschool == self.request.get("highschool"))
        school = query.fetch()
        student = query.get()
        list_template = jinja_env.get_template('templates/highschool.html')
        html = list_template.render({
            "highschool": student.highschool,
            "highschoolList": school,
            "email": student.email
        })
        self.response.write(html)
#DISPLAY EVERYONE IN THE SAME COLLEGE
class RetrieveCollege(webapp2.RequestHandler):
    def get(self):
        query = model.Person.query().filter(model.Person.college == self.request.get("college"))
        school = query.fetch()
        student = query.get()
        list_template = jinja_env.get_template('templates/college.html')
        html = list_template.render({
            "college": student.college,
            "collegeList": school,
            "email": student.email
        })
        self.response.write(html)
#TABS TABS TABS
app = webapp2.WSGIApplication([
    ('/', MainHandler), # asking for slash, construct main handlers
    ('/signup', SignUpHandler),
    ('/list', PersonHandler),
    ('/list/users', PersonFile),
    ('/login', LoginHandler),
    ('/map', MapHandler),
    ('/latlong', Personlatlong),
    ('/profile', RetrieveProfile),
    ('/highschool', RetrieveHighschool),
    ('/college', RetrieveCollege),
    ('/map', MapHandler)
], debug = True)
