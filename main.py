import jinja2
import os
import webapp2
import model
import json
from google.appengine.api import urlfetch
import urllib

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
        person.college = self.request.get("college")
        person.city2 = self.request.get("city2")
        person.state2 = self.request.get("state2")
        trivia_response = urlfetch.fetch("https://maps.googleapis.com/maps/api/geocode/json?address="+urllib.quote_plus(person.highschool + ",+" + person.city1 + ",+" + person.state1)+"&key=AIzaSyDanzu3x3EEBjImVNBU_XZPqzcAK2b-mb4").content
        trivia_as_json = json.loads(trivia_response)
        person.hslat = float(trivia_as_json['results'][0]['geometry']['location']['lat'])
        person.hslong = float(trivia_as_json['results'][0]['geometry']['location']['lng'])
        trivia_response2 = urlfetch.fetch("https://maps.googleapis.com/maps/api/geocode/json?address="+urllib.quote_plus(person.college + ",+" + person.city2 + ",+" + person.state2)+"&key=AIzaSyDanzu3x3EEBjImVNBU_XZPqzcAK2b-mb4").content
        trivia_as_json2 = json.loads(trivia_response2)
        person.collat = float(trivia_as_json2['results'][0]['geometry']['location']['lat'])
        person.collong = float(trivia_as_json2['results'][0]['geometry']['location']['lng'])

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
                "hslat":person.hslat,
                "hslong":person.hslong,
                "collat":person.collat,
                "collong":person.collong
                })
            return latlong
        person_dictionaries= persontodict(all_people)
        self.response.write(json.dumps(person_dictionaries))
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
